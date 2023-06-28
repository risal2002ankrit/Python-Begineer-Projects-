# have a python dictionary that has key/value pain that represent a word and it's defination
# collect input form user, input is a word
# check if the word is in the dictinary
# print the defination


def main():
    word_Dictionary = {
        'hi': 'way of greeting',
        'eyes' : 'an organ for seeing',
        'earth' : 'only a living planet'
    }

    while True:
        word = str.lower(input("enter the word"))
        if word == "":
            break
        if word in word_Dictionary:
            print(word,";",word_Dictionary[word])

main()
