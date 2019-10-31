import word_frequency, dictionary_words, random, sys

def convert_histogram(text):
    # text_stuff = text.split()
    word_counts = word_frequency.histogram(text)
    # print(word_counts)
    return word_counts

def pick_one_word(histogram, rate):
    # https://pynative.com/python-random-choice/
    num_total = 0
    check_start = 0
    check_end = 0
    
    # random.iyuo(0,1)
    one_entry = random.choice(list(histogram))
    return one_entry

def calc_probability(histogram):
    rates = {}

    total_amount = 0
    for i in histogram:
        total_amount += histogram[i]

    for entry in histogram:
        rate = histogram[entry]/total_amount
        rates[entry] = rate

    return rates

if __name__=='__main__':
    # params = sys.argv[1:]
    #Example for use: "one fish two fish red fish blue fish"
    string_of_words = sys.argv[1:]
    # params[0]
    # print(convert_histogram(string_of_words))
    print(pick_one_word(convert_histogram(string_of_words)))
    print("----------")
    calc_probability(convert_histogram(string_of_words))
