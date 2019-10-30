import word_frequency, dictionary_words, random, sys

def convert_histogram(text):
    text_stuff = text.split()
    word_counts = word_frequency.histogram(text_stuff)
    return word_counts

def pick_one_word(histogram):
    # https://pynative.com/python-random-choice/
    one_entry = random.choice(list(histogram))
    return one_entry

if __name__=='__main__':
    params = sys.argv[1:]
    #Example for use: "one fish two fish red fish blue fish"
    string_of_words = str(params[0])
    print(pick_one_word(convert_histogram(string_of_words)))
