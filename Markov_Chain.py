from word_probability import pick_one_word, calc_probability, convert_histogram
from word_frequency import get_words
from dictogram import Dictogram
from string import punctuation

test_string = "I can no longer help what I feel in my heart. What is the point of living anymore? I am the king."

text_words = []
for word in test_string.split():
    clean_word = word.strip(punctuation)
    text_words.append(clean_word)

print(text_words)
