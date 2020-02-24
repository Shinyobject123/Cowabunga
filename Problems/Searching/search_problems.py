'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re

def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

file = open('../Searching/dictionary.txt', 'r')
with open('../Searching/dictionary.txt') as f:
    read_data = f.read()
masterList = split_line(read_data)
bigBoy = ''
for i in range(len(masterList)):
    if len(masterList[i]) > len(bigBoy):
        bigBoy = masterList[i]
print(bigBoy)


#print(file)
# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"
file = open('../Searching/AliceInWonderLand.txt', 'r')
with open('../Searching/AliceInWonderLand.txt') as f:
    read_data = f.read()
masterList2 = split_line(read_data)
print(len(masterList2))

sumNum = 0
for i in range(len(masterList2)):
    sumNum += len(masterList2[i])
print(sumNum/len(masterList2))

# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?

sumAlice = 0
for i in range(len(masterList2)):
    if masterList2[i] == "Alice":
        sumAlice += 1
print(sumAlice)

# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
sevenLetterWords = []
for i in range(len(masterList2)):
    if len(masterList2[i]) == 7:
        sevenLetterWords.append(masterList2[i].upper())
print(sevenLetterWords)

max = 0
ans = -1
runs = 0
for i in range(len(sevenLetterWords)):
    now = 1

    for j in range(i+1, len(sevenLetterWords)):
        if sevenLetterWords[j] == sevenLetterWords[i]:
            now += 1

        if (max < now):
            max = now
            ans = sevenLetterWords[i]
print(ans)


# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

sumChe = 0
sumCat = 0
sumCheCat = 0
for i in range(len(masterList2)):
    if masterList2[i].upper() == "CHESHIRE":
        sumChe += 1
        if masterList2[i+1].upper() == "CAT":
            sumCheCat += 1
    elif masterList2[i].upper() == "CAT":
        sumCat += 1


print(sumChe)
print(sumCat)
print(sumCheCat)





