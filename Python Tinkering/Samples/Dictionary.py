english_japanese = {}

def build_dictionary(english, japanese, image)

def useable_dictionary(word):

    english_japanese = {"ask" : "きく", "eat" : "たべる", "run" : "はしる"}

    translation = english_japanese[word]
    
    return translation

english = raw_input("Input a word: ")
japanese = useable_dictionary(english)
print japanese
