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
        for index in range(len(self.word_list)-1):
            # print(self)
            word = self.word_list[index]
            next_word = self.word_list[index+1]

            if word not in self:
                self[word] = {}
                self[word][next_word] = 1
            else:
                dict_of_counts = self[word]
                if next_word not in dict_of_counts:
                    self[word][next_word] = 1
                else:
                    dict_of_counts[next_word] += 1



    def creating_sentence(self, length = 10):
        """Create sentence using both dictogram and the markov chain just made."""
        adding_word = self.dictionary_histogram.sample()
        last_word = adding_word
        created_sentence = ""
        created_sentence += adding_word+" "
        while length-1 > 0:
            if adding_word in self:
                pass

                # word = "Moove"
                # created_sentence += f"{word} "
                # adding_word = word
            else:
                pass
            length -= 1


        return created_sentence

if __name__=="__main__":
    # test_string = "I am. I was. I can only be. I will be king. It is very tiring. I am best."
    test_string = "I like dogs and you like dogs. I like cats but you hate cats."
    first_chain = Markov_Chain(create_list(test_string))
    print(first_chain)
    print(first_chain.creating_sentence())
