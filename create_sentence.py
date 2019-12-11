import word_probability, word_frequency
from second_Order_MarkovChain import Markov_Chain
from string import punctuation

class created_sentence():
    def __init__(self, length = 20):
        self.length = length

    def create_word_list_from_text_file(self):
        text_words = []
        with open('01-The-Eye-of-the-World-Robert-Jordan copy.txt','r') as f:
            for line in f:
                for word in line.split():
                    clean_word = word.strip(punctuation)
                    text_words.append(clean_word)
        return text_words

    def make_sentence(self):
        markov = Markov_Chain(self.create_word_list_from_text_file(), True)
        # print(markov)
        sentence = markov.creating_sentence(self.length)
        return sentence

if __name__=="__main__":
    sentence = created_sentence()
    actual_sentence = sentence.make_sentence()
    print(actual_sentence)
