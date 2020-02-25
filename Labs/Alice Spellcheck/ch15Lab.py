'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re


def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


with open('./dictionary.txt', 'r') as f:
    dict = [x.strip().upper() for x in f]


def linearSearch():
    print("--- Linear Search ---")

    file = open('./AliceInWonderLand200.txt', 'r')

    for line in file:
        words = (split_line(line))

        for i in range(len(words)):
            word = words[i].upper()
            j = 0
            while j < len(dict) and word != dict[j]:
                j += 1
            if j >= len(dict):
                print(word)

    file.close()
def binarySearch():
    print("--- Binary Search ---")

    file = open('./AliceInWonderLand200.txt', 'r')

    for line in file:
        words = (split_line(line))

        for i in range(len(words)):
            word = words[i].upper()
            found = False
            lower_bound = 0
            upper_bound = len(dict)
            while lower_bound <= upper_bound and not found:
                middle_pos = (upper_bound + lower_bound) // 2
                if dict[middle_pos] < word:
                    lower_bound = middle_pos + 1
                elif dict[middle_pos] > word:
                    upper_bound = middle_pos - 1
                else:
                    found = True
            if not found:
                    print(word)

linearSearch()
binarySearch()

# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.
