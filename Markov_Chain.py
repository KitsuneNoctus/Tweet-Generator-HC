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

#=============Markov Chain Class====================
class Markov_Chain(dict):
    def __init__(self, word_list):
        """Initialize the class and create variables"""

        self.word_list = word_list

    def creating_chain(self):
        """ Creating the Markov Chain """
        for index in range(len(self.word_list)-1):
            print(self)
            # self[self.word_list[index]] = 1
            word = self.word_list[index]
            next_word = self.word_list[index+1]
            if word not in self:
                self[word] = {next_word, 1}
            else:
                self[self.word_list[index]][self.word_list[index+1]] += {self.word_list[index+1],1}

    def creating_sentence(self):
        pass

if __name__=="__main__":
    test_string = "I am. I was. I can only be. I will be king. It is very tiring."
    first_chain = Markov_Chain(create_list(test_string))
    first_chain.creating_chain()
    print(first_chain)
