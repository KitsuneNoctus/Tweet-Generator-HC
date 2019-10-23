import random, sys

def rearrange_Quote(string):
    new_string = ""
    string_list = string.split()
    for word in string.split():
        random_word = string_list[random.randint(0,len(string_list)-1)]
        new_string += (random_word + " ")
        string_list.remove(random_word)
    return new_string

def reverse_Quote(string):
    new_string = ""
    string_list = string.split()
    for word in string.split():
        new_string += (string_list[-1] + " ")
        string_list.remove(string_list[-1])
    return new_string
    pass

if __name__=='__main__':
    params = sys.argv[1:]
    #Example for use: "I am the best"
    string_of_words = str(params[0])
    print(rearrange_Quote(string_of_words))
    #print(reverse_Quote(string_of_words))
    pass
