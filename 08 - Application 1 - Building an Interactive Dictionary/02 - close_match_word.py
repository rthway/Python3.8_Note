import json
from difflib import get_close_matches
data = json.load(open("data.json")) # json file load in python

def translate(word): # define translate function to pick up data from json
    word = word.lower() # input value auto convert to lowercase
    if word in data:
        return data[word]

    # suggst simmilar word
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean %s instead" % get_close_matches(word,data.keys())[0]

    else:
        return "The word does not exist. Please double check it. "

word = input("Enter word: ") # user input

print(translate(word))
