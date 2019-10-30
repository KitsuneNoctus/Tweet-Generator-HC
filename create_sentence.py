import word_frequency, dictionary_words, random, sys

def convert_histogram(text):
    text_stuff = text.split()
    word_counts = word_frequency.histogram(text_stuff)
    return word_counts

if __name__=='__main__':
    params = sys.argv[1:]
    #Example for use: "I am the best"
    string_of_words = str(params[0])
    print(convert_histogram(string_of_words))
