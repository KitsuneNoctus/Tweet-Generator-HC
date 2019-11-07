# To read the words from the dictionary
import random, sys
#using code from spaceman here
# f = open('/usr/share/dict/words','r')
# f.close()
# words_list = words_list.split()

# words_list = []
def get_words():
    #Found this snippet of code from here: https://stackoverflow.com/questions/4666339/python-and-palindromes
    #Look up list comprhension
    words_list = [line.strip() for line in open('/usr/share/dict/words')]
    return words_list


def create_random_sentence(sen_length, word_list):

    sentence = ""
    while sen_length != 0:
        ran_word = random.choice(words_list)
        if sen_length == 1:
            sentence += ran_word
        else:
            sentence += (ran_word + " ")
        sen_length -= 1

    return sentence


if __name__=='__main__':
    params = sys.argv[1:]
    number = int(params[0])
    print(create_random_sentence(number,get_words()))
    #print(reverse_Quote(string_of_words))
    pass
