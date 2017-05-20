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
            print ("Invalid entry, please use .txt file name")
            continue

        for line in crypt_fh:
            crypt_message += line

    return crypt_message

def ceaser_cypher_cracker(crypt_message, sample_frequencies = None):

    letters = letter_counter(crypt_message)
    letters = dict_sorter(letters)
    frequencies = frequency_tabulator(letters)

    try:
        frequencies_plotter(frequencies, sample_frequencies)
        shift = shift_determiner(frequencies, sample_frequencies)
        message = ceasar_solver(crypt_message, shift)
        print (message)

    except:
        print ("Sample.txt not found, unable to provide sample comparison.")
        print ("Cypher frequencies:\n{}"
                .format(frequencies))

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

def ceasar_solver(crypt_message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = ''

    for line in crypt_message:
        line = line.strip()
        for letter in line:
            true_letter = alphabet[(alphabet.find(letter) - shift) % 26]
            message += true_letter

    return message

def code_determiner(crypt_freq, sample_freq):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    crypt_values = crypt_freq.values()
    code = ''
    crypt_max = max(crypt_values)
    threshold = crypt_max * 0.70

    for key in crypt_freq:
        if crypt_freq[key] > threshold:
            code += key

    print (code)

def main():
    decrypt_file = True

    sample_frequencies = sample_loader()

    while decrypt_file:

        crypt_message = file_loader()

        answer = input("Is it a [c]easar or [v]igenere cipher? ")

        try:
            cipher_kind = answer[0].lower()
        except:
            print ("Invalid entry, blank string or non-string provided. Please type 'c' or 'v', respectively, for a ceasar\nor vigenere cipher.")
            continue

        if cipher_kind == 'c':
            ceaser_cypher_cracker(crypt_message, sample_frequencies)
        elif cipher_kind == 'v':
            code = code_determiner(frequencies, sample_frequencies)
        else:
            print ("Invalid entry, Please type 'c' or 'v', respectively, for a ceasar of vigenere cipher.")
            continue

        answer = input("Do you want to continue? (y/n): ")

        try:
            keep_going = answer[0].lower()
            if keep_going == 'n':
                decrypt_file = False
        except:
            print("Invalid entry, continuing...")

main()
