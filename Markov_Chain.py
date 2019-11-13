from word_probability import pick_one_word, calc_probability, convert_histogram
from word_frequency import get_words
from dictogram import Dictogram
from string import punctuation
import random

def create_list(string):
    """Turns string into a list of words"""
    text_words = []
    for word in string.split():
        clean_word = word.strip(punctuation)
        text_words.append(clean_word)

    return text_words

#=============Markov Chain Class====================
class Markov_Chain(dict):
    def __init__(self, word_list):
        """Initialize the class and create variables"""
        self.word_list = word_list
        self.dictionary_histogram = Dictogram(self.word_list)

        """ Creating the Markov Chain """
        #Edit so as to get rid of length of list minus 1 and it doesnt run errors
        for index in range(len(self.word_list)-1):
            word = self.word_list[index]

            if len(self.word_list)==index+1:
                next_word = None
            else:
                next_word = self.word_list[index+1]

            if word not in self:
                small_dicto = Dictogram([next_word])
                self[word] = small_dicto

            else:
                self[word].add_count(next_word)

    def creating_sentence(self, length = 10):
        """Create sentence using both dictogram and the markov chain just made."""
        #Edit so it adds periodss and not spaces at the end of a sentence.
        created_sentence = ""
        adding_word = self.dictionary_histogram.sample()
        created_sentence += adding_word+" "
        length = length - 1

        last_word = adding_word

        while length > 0:
            next_word_for = self[adding_word].sample()
            created_sentence += next_word_for+" "
            adding_word = next_word_for
            # if adding_word in self:
            #
            #     pass
            # else:
            #     pass

            length -= 1


        return created_sentence

if __name__=="__main__":
    # test_string = "I am. I was. I can only be. I will be king. It is very tiring. I am best."
    test_string = "I like dogs and you like dogs. I like cats but you hate cats."
    print(test_string)
    first_chain = Markov_Chain(create_list(test_string))
    print(first_chain)
    print(first_chain.creating_sentence())
