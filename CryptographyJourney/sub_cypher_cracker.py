import numpy as np
import matplotlib.pyplot as plt

def letter_counter(handler):
    letters = {}
    count = 0

    for line in handler:
        line = line.strip()
        for letter in line:
            letter = letter.strip()
            if len(letter) > 0:
                try:
                    letters[letter.lower()] += 1
                except:
                    letters[letter.lower()] = 1

            count += 1

    letters['_count'] = count

    return letters

def dict_sorter(letters):
    ordered_letters = {}
    key_letters = sorted(letters)

    for letter in key_letters:
        ordered_letters[letter] = letters[letter]

    return ordered_letters

def frequency_tabulator(letters):
    frequencies = {}
    count = letters['_count']
    percent = 100

    for letter in letters:
        if letter != '_count':
            letter_frequency = (letters[letter]/count) * percent
            frequencies[letter] = letter_frequency

    return frequencies

def frequencies_plotter(frequencies, sample_frequencies):

    keys_list = list(frequencies.keys())
    values = frequencies.values()
    pos1 = np.arange(len(keys_list))
    width = 1.0

    plt.subplot(221)
    plt.bar(pos1, values, width = width)
    plt.xticks(pos1, keys_list)

    ymax = max(values) + 1
    plt.ylim(0, ymax)

    sample_keys_list = list(sample_frequencies.keys())
    sample_values = sample_frequencies.values()
    pos2 = np.arange(len(sample_keys_list))

    plt.subplot(222)
    plt.bar(pos2, sample_values, width = width)
    plt.xticks(pos2, sample_keys_list)

    ymax = max(sample_values) + 1
    plt.ylim(0, ymax)

    plt.show()

def shift_determiner(crypt_freq, sample_freq):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    crypt_letter_pos = 0
    sample_letter_pos = 0
    crypt_max = max(crypt_freq.values())
    sample_max = max(sample_freq.values())

    for letter, freq in crypt_freq.items():
        if freq == crypt_max:
            crypt_letter_pos = alphabet.find(letter)

    for letter, freq in sample_freq.items():
        if freq == sample_max:
            sample_letter_pos += alphabet.find(letter)

    shift = (crypt_letter_pos - sample_letter_pos) % 26

    return shift

def solve(encrypted_text, shift):
    crypt_fh = open(encrypted_text, 'r')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = ''

    for line in crypt_fh:
        line = line.strip()
        for letter in line:
            true_letter = alphabet[(alphabet.find(letter) - shift) % 26]
            message += true_letter

    return message

def main():
    decrypt_file = True

    while decrypt_file:
        crypt_fh = ''
        sample_text_fh = ''

        encrypted_text = input("Please enter .txt file name: ")

        try:
            crypt_fh = open(encrypted_text, 'r')
        except:
            print ("Invalid entry, please use .txt file name")
            continue

        letters = letter_counter(crypt_fh)
        letters = dict_sorter(letters)
        frequencies = frequency_tabulator(letters)

        try:
            sample_text_fh = open('Sample.txt', 'r')

        except:
            print ("Sample.txt not found, unable to provide sample comparison.")
            print ("Cypher frequencies:\n{}"
                    .format(frequencies))

        sample_letters = letter_counter(sample_text_fh)
        sample_letters = dict_sorter(sample_letters)
        sample_frequencies = frequency_tabulator(sample_letters)

        # print ("Cypher frequencies:\n{}\n Sample frequencies:\n{}"
        #         .format(frequencies, sample_frequencies))

        frequencies_plotter(frequencies, sample_frequencies)

        shift = shift_determiner(frequencies, sample_frequencies)
        message = solve(encrypted_text, shift)
        print (message)

        keep_going = input("Do you want to continue? (y/n): ")

        if keep_going[0].lower() == 'n':
            decrypt_file = False

main()
