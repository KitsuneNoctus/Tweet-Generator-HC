from word_probability import pick_one_word, calc_probability, convert_histogram
from word_frequency import get_words
from dictogram import Dictogram
from listogram import Listogram
from string import punctuation
import random

def create_list(string):
    """Turns string into a list of words"""
    text_words = []
    for word in string.split():
        # clean_word = word.strip(punctuation)
        clean_word = word.strip(punctuation)
        text_words.append(word)

    return text_words

#=============Markov Chain Class====================
class Markov_Chain(dict):
    def __init__(self, word_list, passed_text_list):
        """Initialize the class and create variables"""
        self.passed_text_list = passed_text_list

        if self.passed_text_list == True:
            self.word_list = word_list
        else:
            self.word_list = create_list(word_list)

        self.dictionary_histogram = Dictogram(self.word_list)
        self.listogram = Listogram(self.word_list)

        """ Creating the Markov Chain """
        #Edit so as to get rid of length of list minus 1 and it doesnt run errors
        for index in range(len(self.word_list)-2):
            word = self.word_list[index]
            next_word = self.word_list[index+1]
            word_after_next = self.word_list[index+2]

            if (word,next_word) not in self:
                small_dicto = Dictogram([(next_word,word_after_next)])
                self[(word,next_word)] = small_dicto

            else:
                self[(word,next_word)].add_count((next_word,word_after_next))

    def generate_Markov(self):
        pass

    def creating_sentence(self, length = 10):
        """Create sentence using both dictogram and the markov chain just made."""
        #Edit so it adds periodss and not spaces at the end of a sentence.
        # created_sentence = ""
        sentence_words = []
        #Help from John that really works well
        # adding_word = random.choice([words for words in list(self.keys()) if '^' in words[0] and '^' in words[1]])
        current_state = random.choice(list(self.keys()))
        next_word = current_state[1]
        # created_sentence += ' '.join(adding_word)+" "
        sentence_words.extend(current_state)
        length = length - 2

        # last_word = adding_word
        #Help from John that really works well
        # - - - - - - -
        while True:
            #With Alans Help....A lot of this is....
            if any(punctuation in next_word for punctuation in '.?!'):
                break
            # if '.' not in adding_word[1] and '?' not in adding_word[1] and '!' not in adding_word[1]:
            else:  # all(punctuation not in next_word for punctuation in '.?!'):
                histogram = self[current_state]
                next_state = histogram.sample()
                next_word = next_state[1]
                # created_sentence += next_word_for[1]+" "
                sentence_words.append(next_word)
                # adding_word = next_word_for
                current_state = next_state

        # while length > 0:
        #     if length > 1:
        #         next_word_for = self[adding_word].sample()
        #         created_sentence += next_word_for[1]+" "
        #         adding_word = next_word_for
        #         length -= 1
        #     else:
        #         next_word_for = self[adding_word].sample()
        #         created_sentence += next_word_for[1]
        #         adding_word = next_word_for
        #         length -= 1

        created_sentence = ' '.join(sentence_words).capitalize()
        return created_sentence

if __name__=="__main__":
    # test_string = "I am. I was. I can only be. I will be king. It is very tiring. I am best."
    test_string = "I like dogs and you like dogs. I like cats but you hate cats. I like I like I like I like I like I like. cry."
    print(test_string)
    first_chain = Markov_Chain(test_string, False)
    print(first_chain)
    print(first_chain.creating_sentence())
