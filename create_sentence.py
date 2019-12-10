import word_probability, word_frequency
from second_Order_MarkovChain import Markov_Chain
from string import punctuation
class created_sentence():
    def init(self, length = 20):
        self.length = length
        
        text_words = []
        with open('pygmalion.txt','r') as f:
            for line in f:
                for word in line.split():
                    clean_word = word.strip(punctuation)
                    text_words.append(clean_word)

        markov = Markov_Chain(text_words)
        # print(markov)
        sentence = markov.creating_sentence(length)
        return sentence

print(create_actual_sentence())
