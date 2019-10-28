# Counts the number of times each word in a piece of text appears
# https://stackoverflow.com/questions/37221307/how-do-i-strip-all-leading-and-trailing-punctuation-in-python
from string import punctuation

def get_words():
    #Found this snippet of code from here: https://stackoverflow.com/questions/4666339/python-and-palindromes
    #Look up list comprhension
    # text_words = [line.strip() for line in open('les_miserables.txt')]
    text_words = []
    with open('pygmalion.txt','r') as f:
        for line in f:
            for word in line.split():
                clean_word = word.strip(punctuation)
                text_words.append(clean_word)
    return text_words

def histogram(text):
    '''
    takes a source_text argument (can be either a filename or the contents of the file as a string,
    your choice) and return a histogram data structure that stores each unique word along with the number
    of times the word appears in the source text.
    '''
    dictionary_for_text = {}
    list_of_lists = []
    list_of_tuples = []
    count_of_words = []

    all_counts = []

    for word in text:
        if word not in dictionary_for_text:
            dictionary_for_text[word] = 1
        else:
            dictionary_for_text[word] += 1

    for entry in dictionary_for_text:
        next_entry = [entry,dictionary_for_text[entry]]
        list_of_lists.append(next_entry)

        list_of_tuples.append(tuple((entry,dictionary_for_text[entry])))

    for entry in dictionary_for_text:
        number_count = dictionary_for_text[entry]
        list_or_wordss = []
        if number_count not in all_counts:
            all_counts.append(number_count)
            # list_or_words = []
            for entry in dictionary_for_text:
                if dictionary_for_text[entry] == number_count:
                    list_or_wordss.append(entry)

            count_of_words.append(tuple((number_count,list_or_wordss)) )

    # print(count_of_words)
    return dictionary_for_text

def unique_words(histogram):
    '''
    takes a histogram argument and returns the total count of unique words in the histogram.
    Return the amount of different words.
    '''
    # unique_count = 0
    # for key in histogram:
    #     if histogram[key] == 1:
    #         unique_count += 1

        # if key == "under":
        #     unique_count += histogram[key]
    # Using this method on advice from David
    return len(histogram)
    # unique_count

def frequency(histogram,word):
    '''
    takes a word and histogram argument and returns the number of times that word appears in a text.
    For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.
    '''
    for key in histogram:
        if word == key:
            return histogram[key]


if __name__=='__main__':
    user_input = input("Enter word looking for: ")
    print(frequency(histogram(get_words()),user_input))
    # print(unique_words(histogram(get_words())))
    # print(histogram(get_words()))
