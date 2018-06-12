import audioread
import os
import random
import wave
import pickle

def run():
	answer = input("Press '1' to build a song ")

	return answer == '1'

def main():
	music_set = {}
	main_path = "~/Music/iTunes/iTunes Media/Music/The Planet Smashers/Mighty/"
	file_name = "01 Mighty.m4a"
	try:
		load_file_name = input("Please enter music set name: ")
		music_set = pickle.load(load_file_name, "rb" )
	except:
		# for directory in os.listdir(os.path.expanduser(main_path) ):
		# 	dir_path = main_path + directory
		# for file_name in os.listdir(os.path.expanduser(main_path)):

		if file_name.endswith(".m4a"):
			print("Adding '" + file_name + "' to knowledge base...")
			file_path = main_path + file_name
			fh = audioread.audio_open(os.path.expanduser(file_path) )
			song = []

			for data in fh:
				song += data.split()

			for i in range(len(song)-5):
				if (i%1000000 == 0):
					print(len(song)-5-i)

				cause = (song[i], song[i+1], song[i+2], song[i+3])
				effect = (song[i+4], song[i+5])
				if (cause not in music_set):
					music_set[cause] = [effect]
				else:
					music_set[cause].append(effect)
				if (i == len(song)-6):
					music_keys = list(music_set.keys())
					cause = (song[i+2], song[i+3], song[i+4], song[i+5])
					effect = music_set[music_keys[0]]
					music_set[cause] = [effect]

			fh.close()
			print(len(music_set))
			pickle.dump(music_set, open("MusicSet1.pickle", "wb" ) )

	running = run()
	while(running):
		print("Building song...")

		ms_keys = list(music_set.keys())
		current_key = ms_keys[random.randint(0, len(ms_keys) - 1)]
		length = (random.randint(0, 4000) + 6000)

		first_bit = current_key[0]
		second_bit = current_key[1]
		third_bit = current_key[2]
		fourth_bit = current_key[3]
		new_song = [first_bit, second_bit, third_bit, fourth_bit]

		while(len(new_song) < length):
			if (len(new_song)%100000 == 0):
				print(length - len(new_song))

			bit_index = random.randint(0, len(music_set[current_key] ) - 1)
			first_bit = music_set[current_key][bit_index][0]
			second_bit = music_set[current_key][bit_index][1]
			new_song += [first_bit, second_bit]

			current_key = (third_bit, fourth_bit, first_bit, second_bit)

			# while(current_key not in ms_keys):
			# 	current_key = ms_keys[random.randint(0, len(ms_keys) ) ]

			third_bit = first_bit
			fourth_bit = second_bit

		save_file = wave.open(input("Please enter file save name: ") + ".wav", 'wb')

		save_file.setnchannels(2)
		save_file.setsampwidth(2)
		save_file.setframerate(44100)

		save_file.writeframesraw(bytes(new_song) )
		save_file.close()

		running = run()

main()
