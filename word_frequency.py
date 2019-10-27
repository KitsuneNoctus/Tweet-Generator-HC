# Counts the number of times each word in a piece of text appears

def get_words():
    #Found this snippet of code from here: https://stackoverflow.com/questions/4666339/python-and-palindromes
    #Look up list comprhension
    # text_words = [line.strip() for line in open('les_miserables.txt')]
    text_words = []
    with open('les_miserables.txt','r') as f:
        for line in f:
            for word in line.split():
                text_words.append(word)
    return text_words
def histogram(text):
    '''
    takes a source_text argument (can be either a filename or the contents of the file as a string,
    your choice) and return a histogram data structure that stores each unique word along with the number
    of times the word appears in the source text.
    '''
    dictionary_for_text = {}
    for word in text:
        if word not in dictionary_for_text:
            dictionary_for_text[word] = 1
        else:
            dictionary_for_text[word] += 1

    return dictionary_for_text
    pass

def unique_words(histogram):
    '''
    takes a histogram argument and returns the total count of unique words in the histogram.
    '''

    pass

def frequency(histogram,words):
    '''
    takes a word and histogram argument and returns the number of times that word appears in a text.
    For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.
    '''
    pass

# print(histogram(get_words()))
print(get_words())
