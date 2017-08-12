import random

ALL_TILES = ['0', '1', '2', '3', '01', '02', '03', '12', '13', '23', '012', '013', '023', '123']

ONE_SIDED = {
    '0' : [[1, 0], [0, -1], [-1, 0]],
    '1' : [[0, 1], [0, -1], [-1, 0]],
    '2' : [[0, 1], [1, 0], [-1, 0]],
    '3' : [[0, 1], [1, 0], [0, -1]]
    }
TWO_SIDED = {
    '01' : [[0, -1], [-1, 0]],
    '02' : [[1, 0], [-1, 0]],
    '03' : [[1, 0], [0, -1]],
    '12' : [[0, 1], [-1, 0]],
    '13' : [[0, 1], [0, -1]],
    '23' : [[0, 1], [1, 0]]
    }

def build_path():
    path = {}

    THREE_SIDED = {
        '123' : [0, 1],
        '023' : [1, 0],
        '013' : [0, -1],
        '012' : [-1, 0]
        }

    level = input("What is your level? ")

    path_length = int(level) + 1
    i = 0
    current_pos = (0, 0)
    next_pos = [0, 0]
    last_tile = ''
    side_in = None
    side_out = None

    while (i < path_length):
        if (i == 0):
            start_tiles = []
            j = 0

            for side in ALL_TILES:
                if (len(side) == 3):
                    start_tiles.append(side)

            start_tile_index = random.randrange(len(start_tiles))
            tile_name = start_tiles[start_tile_index]
            path[current_pos] = tile_name

            next_pos[0] += THREE_SIDED[tile_name][0]
            next_pos[1] += THREE_SIDED[tile_name][1]
            current_pos = tuple(next_pos)
            last_tile = tile_name

            if (next_pos[1] > 0):
                side_out = 0
            elif (next_pos[1] < 0):
                side_out = 2
            if (next_pos[0] > 0):
                side_out = 1
            elif (next_pos[0] < 0):
                side_out = 3

            side_in = (side_out + 2) % 4
            print("side_in {}".format(side_in))

        elif ((i > 0) and (i < (path_length - 1))):
            j = 0
            tiles = []

            while (j < 4):
                tiles += check_tiles(j, last_tile, side_in, top = 2)

                j += 1

            tile_index = random.randrange(len(tiles))
            tile_name = tiles[tile_index]
            path[current_pos] = tile_name

            potential_pos = collision_check(path, current_pos, tile_name)
            last_pos = current_pos
            current_pos = potential_pos[random.randrange(len(potential_pos))]
            last_tile = tile_name

            next_pos[0] = current_pos[0] - last_pos[0]
            next_pos[1] = current_pos[1] - last_pos[1]

            if (next_pos[1] > 0):
                side_out = 0
            elif (next_pos[1] < 0):
                side_out = 2
            if (next_pos[0] > 0):
                side_out = 1
            elif (next_pos[0] < 0):
                side_out = 3

            side_in = (side_out + 2) % 4
            print("side_in {}".format(side_in))

        else:
            j = 0
            end_tiles = []

            while (j < 4):
                end_tiles += check_tiles(j, last_tile, side_in, iso = 3)
                j += 1

            end_tile_index = random.randrange(len(end_tiles))
            tile_name = end_tiles[end_tile_index]
            path[current_pos] = tile_name

        i += 1

    return path

def check_tiles(side, last_tile, side_in, iso = None, top = None):
    tiles = []

    if (str(side) not in last_tile):
        for tile in ALL_TILES:
            if str(side_in) not in tile:
                if (iso == None):
                    if (len(tile) <= top):
                        if tile not in tiles:
                            tiles.append(tile)
                else:
                    if (len(tile) == iso):
                        if tile not in tiles:
                            tiles.append(tile)

    return tiles

def collision_check(path, current_pos, tile_name):
    potential_openings = []
    openings = []

    if tile_name in ONE_SIDED:
        potential_openings += ONE_SIDED[tile_name]
    else:
        potential_openings += TWO_SIDED[tile_name]

    for potential_opening in potential_openings:
        potential_pos = ((current_pos[0] + potential_opening[0]),
                            (current_pos[1] + potential_opening[1]))
        if potential_pos not in path:
            openings.append(potential_pos)

    return openings


path = build_path()
print(path)
