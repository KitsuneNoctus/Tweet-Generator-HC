import word_frequency, dictionary_words, random, sys

def convert_histogram(): #text
    # text_stuff = text.split()
    # word_counts = word_frequency.histogram(text)
    word_counts = word_frequency.histogram(word_frequency.get_words())
    # print(word_counts)
    return word_counts

def pick_one_word(rates):
    # https://pynative.com/python-random-choice/
    dart = random.random()
    num_total = 0
    check_start = 0
    check_end = 0
    for rate in rates:
        check_end += rates[rate]
        if dart <= check_end and dart > check_start:
            return rate
        else:
            check_start = check_end


    # # random.iyuo(0,1)
    # one_entry = random.choice(list(histogram))
    # return one_entry

def calc_probability(histogram):
    rates = {}
    total_amount = 0

    for i in histogram:
        total_amount += histogram[i]

    for entry in histogram:
        rate = histogram[entry]/total_amount
        rates[entry] = rate

    return rates

def check_correct_probability(repeat):
    fish_count = 0
    red_count = 0
    blue_count = 0
    one_count = 0
    two_count = 0
    for _ in range(0,repeat):
        word = pick_one_word(calc_probability(convert_histogram(string_of_words)))
        if word == "fish":
            fish_count += 1
        elif word == "blue":
            blue_count += 1
        elif word == "red":
            red_count += 1
        elif word == "one":
            one_count += 1
        elif word == "two":
            two_count += 1
    print(f"fish: {fish_count}")
    print(f"red: {red_count}")
    print(f"blue: {blue_count}")
    print(f"one: {one_count}")
    print(f"two: {two_count}")


if __name__=='__main__':
    # params = sys.argv[1:]
    #Example for use: "one fish two fish red fish blue fish"
    string_of_words = sys.argv[1:]
    # params[0]
    # print(convert_histogram(string_of_words))

    print("----------")
    print(calc_probability(convert_histogram(string_of_words)))
    print("----------")
    print(pick_one_word(calc_probability(convert_histogram(string_of_words))))
    print("----------")
    # calc_probability(convert_histogram(string_of_words))
    check_correct_probability(10000)
