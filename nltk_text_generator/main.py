import nltk
from nltk.tokenize import RegexpTokenizer
from collections import Counter

nltk.download("punkt")

fileName = input("File name: ")
source = open(fileName, "r", encoding="utf-8")

lines = source.readlines()
text = ""

source.close()

for line in lines:
    text += line

tokenizer = RegexpTokenizer(r'[\s\t\n]+', gaps=True)
corpus = tokenizer.tokenize(text)

# STAGE 1 TEST
'''
print("Corpus statistics")
print(f"All tokens: {len(corpus)}")
print(f"Unique tokens: {len(set(corpus))}")

while True:
    index = input()
    if index == "exit":
        break
    elif index.isdigit() or (index.startswith("-") and index[1:].isdigit()):
        index = int(index)
        if index <= len(corpus):
            print(corpus[index])
        else:
            print("Index Error. Please input an integer that is in the range of the corpus.")
    else:
        print("Type Error. Please input an integer.")
'''

bigrams = [[corpus[i], corpus[i+1]] for i in range(len(corpus)-1)]

# STAGE 2 TEST
'''
print(f"Number of bigrams: {len(bigrams)}")

while True:
    index = input()
    if index == "exit":
        break
    elif index.isdigit() or (index.startswith("-") and index[1:].isdigit()):
        index = int(index)
        if index <= len(bigrams):
            print(f"Head: {bigrams[index][0]}  Tail: {bigrams[index][1]}")
        else:
            print("Index Error. Please input a value that is not greater than the number of all bigrams.")
    else:
        print("Type Error. Please input an integer.")
'''

# This is to be updated (not working at the moment)
bigram_dictionary = {}

for head, tail in bigrams:
    bigram_dictionary.setdefault(head, []).append(tail)

for head in bigram_dictionary:
    bigram_dictionary[head] = Counter(bigram_dictionary[head])

while True:
    head_request = input()
    if (head_request in bigram_dictionary) or head_request == "exit":
        break
    else:
        print(head_request)
        print("The requested word is not in the model. Please input another word.")

while True:
    if head_request == "exit":
        break
    else:
        print(f"Head: {head_request}")
        for tail in bigram_dictionary[head_request]:
            print(f"Tail: {tail}:\tCount: {bigram_dictionary[head_request][tail]}")
