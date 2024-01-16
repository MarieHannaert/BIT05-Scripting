#!/usr/bin/python3
def words_seperator(sequence_of_words, seperate_character):
    words=sequence_of_words.split(seperate_character)
    words.sort()
    joined_words=seperate_character.join(words)
    print(joined_words)
    return joined_words
    

sequence_of_words=input("Give a sequence of words: ")
seperate_character=input("Give a character that seperates: ")
joined_words=words_seperator(sequence_of_words, seperate_character)
print("the sorted and joined words are: {}".format(joined_words))

