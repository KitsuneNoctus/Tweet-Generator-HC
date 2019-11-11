from word_probability import pick_one_word, calc_probability, convert_histogram
from word_frequency import get_words
from dictogram import Dictogram
from string import punctuation

test_string = "I can no longer help what I feel in my heart. What is the point of living anymore? I am the king."

def create_list(string):
    text_words = []
    for word in string.split():
        clean_word = word.strip(punctuation)
        text_words.append(clean_word)

    return text_words

class Markov_Chain():
    def __init__(self, word_list):

print(create_list(test_string))
markov_dict = {}

for word in text_words:

    if word not in markov_dict:
        markov_dict[word] = 1
    else:
        self[word] += 1
