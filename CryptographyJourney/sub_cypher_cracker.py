import numpy as np
import matplotlib.pyplot as plt

def sample_loader():
    sample_frequencies = ''
    sample_message = ''

    try:
        sample_text_fh = open('Sample.txt', 'r')

        for line in sample_text_fh:
            sample_message += line

        sample_letters = letter_counter(sample_message)
        sample_letters = dict_sorter(sample_letters)
        sample_frequencies = frequency_tabulator(sample_letters)
    except:
        sample_frequencies = None
        print ("Sample.txt not found, unable to provide sample comparison.")

    return sample_frequencies

def file_loader():
    invalid_entry = True
    crypt_message = ''

    while invalid_entry:

        encrypted_text = input("Please enter .txt file name: ")

        try:
            crypt_fh = open(encrypted_text, 'r')
            invalid_entry = False
        except:
            print ("Invalid entry, file not found.")
            continue

        for line in crypt_fh:
            crypt_message += line

    return crypt_message

def letter_counter(message):
    letters = {}
    count = 0

    for letter in message:
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

    plt.subplot(121)
    plt.bar(pos1, values, width = width)
    plt.xticks(pos1, keys_list)

    ymax = max(values) + 1
    plt.ylim(0, ymax)

    sample_keys_list = list(sample_frequencies.keys())
    sample_values = sample_frequencies.values()
    pos2 = np.arange(len(sample_keys_list))

    plt.subplot(122)
    plt.bar(pos2, sample_values, width = width)
    plt.xticks(pos2, sample_keys_list)

    ymax = max(sample_values) + 1
    plt.ylim(0, ymax)

    plt.show()

def code_determiner(crypt_message, sample_freq = None):
    uncracked = True
    cipher_length = 0

    while uncracked:
        cipher_length += 1
        split_letters = {}
        key_letter_groups = []
        keywords = []

        for idx, letter in enumerate(crypt_message):
            try:
                split_letters[idx % cipher_length] += letter
            except:
                split_letters[idx % cipher_length] = letter

        for position in split_letters:
            crypt_split = split_letters[position]

            letters = letter_counter(crypt_split)
            letters = dict_sorter(letters)
            frequencies = frequency_tabulator(letters)

            frequencies_plotter(frequencies, sample_freq)
            key_letter_groups.append(keyword_determiner(frequencies))

        keywords = keyword_builder(key_letter_groups, cipher_length)

        for key in keywords:
            keyword = keywords[key]
            print(key, keyword)
            keyword_cracker(crypt_message, keyword, sample_freq)
            print('\n')

        msg = "Is the message cracked? (y/n) "
        invalid_response = "Neither 'y' nor 'n' entered, exiting cracking."
        uncracked = quit(msg, invalid_response)

def keyword_builder(key_letter_groups, cipher_length):
    print(key_letter_groups)
    keywords = keyword_constructor(key_letter_groups)
    return keywords

def keyword_constructor(key_letter_groups):
    # self expanding for-loop sequence to account for lengthening
    # cypher_length
    keywords = {}

    if len(key_letter_groups) > 5:
        for idx1, letter1 in enumerate(key_letter_groups[0]):
            for idx2, letter2 in enumerate(key_letter_groups[1]):
                for idx3, letter3 in enumerate(key_letter_groups[2]):
                    for idx4, letter4 in enumerate(key_letter_groups[3]):
                        for idx5, letter5 in enumerate(key_letter_groups[4]):
                            for idx6, letter6 in enumerate(key_letter_groups[5]):
                                keywords[(idx1, idx2, idx3, idx4, idx5, idx6)] = letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    elif len(key_letter_groups) > 4:
        for idx1, letter1 in enumerate(key_letter_groups[0]):
            for idx2, letter2 in enumerate(key_letter_groups[1]):
                for idx3, letter3 in enumerate(key_letter_groups[2]):
                    for idx4, letter4 in enumerate(key_letter_groups[3]):
                        for idx5, letter5 in enumerate(key_letter_groups[4]):
                            keywords[(idx1, idx2, idx3, idx4, idx5)] = letter1 + letter2 + letter3 + letter4 + letter5
    elif len(key_letter_groups) > 3:
        for idx1, letter1 in enumerate(key_letter_groups[0]):
            for idx2, letter2 in enumerate(key_letter_groups[1]):
                for idx3, letter3 in enumerate(key_letter_groups[2]):
                    for idx4, letter4 in enumerate(key_letter_groups[3]):
                        keywords[(idx1, idx2, idx3, idx4)] = letter1 + letter2 + letter3 + letter4
    elif len(key_letter_groups) > 2:
        for idx1, letter1 in enumerate(key_letter_groups[0]):
            for idx2, letter2 in enumerate(key_letter_groups[1]):
                for idx3, letter3 in enumerate(key_letter_groups[2]):
                    keywords[(idx1, idx2, idx3)] = letter1 + letter2 + letter3
    elif len(key_letter_groups) > 1:
        for idx1, letter1 in enumerate(key_letter_groups[0]):
            for idx2, letter2 in enumerate(key_letter_groups[1]):
                keywords[(idx1, idx2)] = letter1 + letter2
    else:
        for idx, letter in enumerate(key_letter_groups):
            keywords[(idx)] = letter

    return keywords

def keyword_determiner(crypt_freq):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    crypt_letter_pos = 0
    keyword = ""
    crypt_max = max(crypt_freq.values())

    for letter, freq in crypt_freq.items():
        if freq == crypt_max:
            keyword += letter

    return keyword

def key_shift_determiner(key_letter, sample_freq):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    crypt_letter_pos = 0
    sample_letter_pos = 0
    sample_max = max(sample_freq.values())

    for letter, freq in sample_freq.items():
        if freq == sample_max:
            sample_letter_pos += alphabet.find(letter)

    crypt_letter_pos = alphabet.find(key_letter)

    key_shift = (crypt_letter_pos - sample_letter_pos) % 26

    return key_shift

def ceasar_solver(crypt_message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = ''

    for line in crypt_message:
        line = line.strip()
        for letter in line:
            true_letter = alphabet[(alphabet.find(letter) - shift) % 26]
            message += true_letter

    return message

def keyword_cracker(crypt_message, keyword, sample_freq):
    shift = []
    message = ""
    for key_idx, key_letter in enumerate(keyword):
        shift.append(key_shift_determiner(key_letter, sample_freq))

    for crypt_idx, crypt_letter in enumerate(crypt_message):
        for shift_idx, pos in enumerate(shift):
            if crypt_idx % len(shift) == shift_idx:
                message += ceasar_solver(crypt_letter, pos)

    print (message)

def quit(message, invalid_response):
    invalid_response = True

    while invalid_response:
        answer = input(message)

        try:
            quit = answer.lower()[0]
        except:
            print ("Invalid response, please enter 'y' for yes or 'n' for no")
            continue

        if quit == 'y':
            return False

        elif quit == 'n':
            return True

        else:
            print (invalid_response)
            return True

def main():
    decrypt_file = True

    sample_frequencies = sample_loader()

    while decrypt_file:

        crypt_message = file_loader()

        keyword = input("What is the a keyword? Enter '!' if there isn't one:\n")
        keyword = keyword.lower()

        if keyword == "!":
            code = code_determiner(crypt_message, sample_frequencies)
        else:
            keyword_cracker(crypt_message, keyword, sample_frequencies)

        msg = "Would you like to quit? (y/n) "
        invalid_response = "Neither 'y' nor 'n' entered, exiting program."
        decrypt_file = quit(msg, invalid_response)

main()
