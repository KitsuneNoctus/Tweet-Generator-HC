import random, sys

def rearrange_Quote(string):
    """Randomizes the entire string order"""
    new_string = ""
    string_list = string.split()
    for word in string.split():
        random_word = random.choice(string_list)
        if len(string_list)<2:
            new_string += (random_word)
        else:
            new_string += (random_word + " ")
        string_list.remove(random_word)
    return new_string + "."

def test_rearrange_Quote():
    string_test = "I am the greatest."

    assert string_test != rearrange_Quote(string_test)

def reverse_Quote(string):
    """Will put the entire string backwards"""
    new_string = ""
    string_list = string.split()
    for word in string.split():
        new_string += (string_list[-1] + " ")
        string_list.remove(string_list[-1])
    return new_string

if __name__=='__main__':
    params = sys.argv[1:]
    #Example for use: "I am the best"
    string_of_words = str(params[0])
    print(rearrange_Quote(string_of_words))
    # print(reverse_Quote(string_of_words))
