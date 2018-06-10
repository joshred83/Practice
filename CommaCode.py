def listToString(some_list):
    your_string = ''
    for i in range(len(some_list)-1):
        your_string += some_list[i] + ', '

    your_string += 'and ' + some_list[len(some_list) - 1] + '.'
    return your_string


spam = ['apples', 'bananas', 'tofu', 'cats']


spam_string = listToString(spam)

print(spam_string)
