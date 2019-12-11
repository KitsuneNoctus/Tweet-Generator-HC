import word_probability, word_frequency
from second_Order_MarkovChain import Markov_Chain
from string import punctuation
import nltk
import re

class created_sentence():
    def __init__(self, length = 20):
        self.length = length

    def create_word_list_from_text_file(self):
        text_words = []
        with open('01-The-Eye-of-the-World-Robert-Jordan copy.txt','r') as f:
            for line in f:
                for word in line.split():
                    #clean_word = word.strip(punctuation)
                    # clean_word = word.strip(punctuation)
                    # text_words.append(clean_word)
                    text_words.append(word)
        return text_words

    def make_sentence(self, use_text):
        if use_text == True:
            markov = Markov_Chain(self.create_word_list_from_text_file(), True)
        else:
            markov = Markov_Chain("“^ ^ Ilyena! ^ ^ My love, where are you?” ^ ^ The edge of his pale gray cloak trailed through blood as he stepped across the body of a woman, her golden-haired beauty marred by the horror of her last moments, her still-open eyes frozen in disbelief.",False)
        # print(markov)
        sentence = markov.creating_sentence(self.length)
        return sentence

if __name__=="__main__":
    # sentence = created_sentence()
    # actual_sentence = sentence.make_sentence(True)
    # print(actual_sentence)
    sentence = created_sentence()
    actual_sentence = sentence.make_sentence(False)
    print(actual_sentence)
