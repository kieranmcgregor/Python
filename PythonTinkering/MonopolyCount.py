import random

TEST_COUNT = 10000
PERCENT = 100
BOARD_SQUARES = 40
MAX_ROLL = 6
MIN_ROLL = 1
GO_TO_JAIL = 30
DIST_TO_JAIL = 20
SETS = ((1, 3),				#Browns
		(5, 15, 25, 35),	#Railroads
		(6, 8, 9),			#Blues
		(11, 13, 14),		#Purples
		(12, 28),			#Utilities
		(16, 18, 19),		#Oranges
		(21, 23, 24),		#Reds
		(26, 27, 29),		#Yellows
		(31, 32, 34),		#Greens
		(37, 39))			#Dark Blues

SET_COLOURS = ('Browns',
				'Railroads',
				'Blues',
				'Purples',
				'Utilities',
				'Oranges',
				'Reds',
				'Yellows',
				'Greens',
				'Dark Blues')
SQUARE_NAMES = ("GO",
				"Mediteranean Avenue",
				"Community Chest",
				"Baltic Avenue",
				"Income Tax",
				"Reading Railroad",
				"Oriental Avenue",
				"Chance",
				"Vermont Avenue",
				"Connecticut Avenue",
				"Jail",
				"St. Charles Place",
				"Electric Company",
				"States Avenue",
				"Virginia Avenue",
				"Pennsylvania Railroad",
				"St. James Place",
				"Community Chest",
				"Tennessee Avenue",
				"New York Avenue",
				"Free Parking",
				"Kentucky Avenue",
				"Chance",
				"Indiana Avenue",
				"Illinois Avenue",
				"B & O Railroad",
				"Atlantic Avenue",
				"Ventnor Avenue",
				"Water Works",
				"Marvin Gardens",
				"Go To Jail",
				"Pacific Avenue",
				"North Carolina Avenue",
				"Community Chest",
				"Pennsylvannia Avenue",
				"Short Line",
				"Chance",
				"Park Place",
				"Luxury Tax",
				"Boardwalk")

def roll_dice():
	current_roll = random.randint(MIN_ROLL, MAX_ROLL)
	current_roll += random.randint(MIN_ROLL, MAX_ROLL)
	#print(current_roll)
	
	return current_roll

def run_test():
	rolls = []
		
	for i in range(MAX_ROLL*2 - 1):
		rolls.append(0)
		
	for i in range(TEST_COUNT):
		rolls[roll_dice() - 2] += 1
	
	for roll in rolls:
		print(roll/TEST_COUNT*100)

def main():
	#print(SQUARE_NAMES[GO_TO_JAIL], SQUARE_NAMES[(GO_TO_JAIL + DIST_TO_JAIL) % BOARD_SQUARES ])
	position = 0
	#mock_pos = 0
	places = []
	longest_name_len = 0
	set_freq = []

	answer = input("Test?")
	
	if (len(answer) > 0 and answer.lower()[0] == 'y'):
		run_test()

	for i in range(BOARD_SQUARES):
		places.append(0)
	
	for i in range(TEST_COUNT):
		dice_roll = roll_dice()
		#mock_pos += dice_roll
		position = (position + dice_roll) % BOARD_SQUARES
		#print(str(dice_roll), str(position), str(mock_pos % BOARD_SQUARES) )

		if (position == GO_TO_JAIL):
			places[position] += 1
			position = (position + DIST_TO_JAIL) % BOARD_SQUARES

		places[position] += 1

	for i in range(BOARD_SQUARES):
		print('%25.25s' %SQUARE_NAMES[i] + ': %3.2f' %(places[i]/TEST_COUNT*PERCENT) + '%')
	
	for place_set in SETS:
		total = 0
		for i in place_set:
			total += places[i]
		set_freq.append(total)
	
	print()
	#print(set_freq)
	for i in range(len(set_freq) ):
		print('%25.10s' %SET_COLOURS[i] + ': %3.2f' %(set_freq[i]/TEST_COUNT * PERCENT) )

if __name__ == '__main__':
	main()