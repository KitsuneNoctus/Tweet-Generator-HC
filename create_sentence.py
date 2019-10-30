import word_frequency, dictionary_words, random, sys
text = 'one fish two fish red fish blue fish'

text_stuff = text.split()
word_counts = word_frequency.histogram(text_stuff)
print(word_counts)
