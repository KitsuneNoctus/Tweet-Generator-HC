from word_probability import pick_one_word, calc_probability, convert_histogram
from word_frequency import get_words
from dictogram import Dictogram
from string import punctuation

test_string = "I am. I was. I can only be. I will be king. It is very tiring."

def create_list(string):
    """Turns string into a list of words"""
    text_words = []
    for word in string.split():
        clean_word = word.strip(punctuation)
        text_words.append(clean_word)

    return text_words

print(create_list(test_string))
#=============Markov Chain Class====================
class Markov_Chain(dict):
    def __init__(self, word_list):
        """Initialize the class and create variables"""

        self.word_list = word_list

    def creating_chain():
        """ Creating the Markov Chain """
        for word in self.word_list:
            if word not in self.markov_dict:
                self.markov_dict[word] = {}
            else:
                self[word] += 1

    def creating_sentence():
        pass

if __name__=="__main__":
    pass
