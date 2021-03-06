import random
import nltk
from nltk.tokenize import RegexpTokenizer
from collections import Counter, defaultdict

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

bigram_dictionary = defaultdict(list)

for head, tail in bigrams:
    bigram_dictionary.setdefault(head, []).append(tail)

# bigram_dictionary = {head1 : [tail11, tail12], head2: [tail21, tail22],...}

dict2 = defaultdict(dict)
for head in bigram_dictionary:
    dict2[head] = Counter(bigram_dictionary[head])

# dict2 = {head1 : {tail11: f11, tail12: f12}, head2: {tail21: f21, tail22: f22},...}

# STAGE 3 TEST
'''
while True:
    head_request = input()
    if head_request == "exit":
        break
    elif head_request in dict2:
        print(f"Head: {head_request}")
        for tail in dict2[head_request]:
            print(f"Tail: {tail} Count: {dict2[head_request][tail]}")
    else:
        print(f"Head: {head_request}")
        print("Key Error. The requested word is not in the model. Please input another word.\n")
'''

# STAGE 4 TEST
'''
no_of_words = 1
sentence = []

while True:
    first_word = random.choice(corpus)
    if first_word[0].isupper():
        break
sentence.append(first_word)

for no_of_sentences in range(10):

    while no_of_words != 10:
        population = list(set(bigram_dictionary[first_word]))
        weights = []
        for tail in dict2[first_word]:
            weights.append(dict2[first_word][tail])
        second_word = random.choices(population, weights)
        sentence.append(second_word[0])
        first_word = second_word[0]
        no_of_words += 1
    print(' '.join(sentence))
    no_of_words = 0
    first_word = sentence[-1]
    sentence.clear()
'''

# STAGE 5 TEST
'''
no_of_words = 1
sentence = []


def findif(sentence):
    lista = sentence
    for i in range(4, len(lista)):
        if lista[i].endswith(".") or lista[i].endswith("?") or lista[i].endswith("!"):
            return i
    return -1


for i in range(10):
    while True:
        first_word = random.choice(corpus)
        if first_word[0].isupper() and (("." not in first_word) and ("!" not in first_word) and ("?" not in first_word)):
            break
    sentence.append(first_word)

    while True:
        population = list(set(bigram_dictionary[first_word]))
        weights = []
        for tail in dict2[first_word]:
            weights.append(dict2[first_word][tail])
        second_word = random.choices(population, weights)
        if no_of_words > 5:
            if sentence[-1].endswith(".") or sentence[-1].endswith("!") or sentence[-1].endswith("?"):
                break
        sentence.append(second_word[0])
        first_word = second_word[0]
        no_of_words += 1

    index = findif(sentence)
    sentence = sentence[:index+1]
    print(' '.join(sentence))
    no_of_words = 0
    sentence.clear()
'''


# STAGE 6
trigrams = [[corpus[i], corpus[i+1], corpus[i+2]] for i in range(len(corpus)-2)]
trigrams2 = [[trigrams[i][0] + " " + trigrams[i][1], trigrams[i][2]] for i in range(len(trigrams))]
trigram_heads = [trigrams2[i][0] for i in range(len(trigrams))]
trigram_dictionary = defaultdict(list)
for head, tail in trigrams2:
    trigram_dictionary.setdefault(head, []).append(tail)

dict3 = defaultdict(dict)
for head in trigram_dictionary:
    dict3[head] = Counter(trigram_dictionary[head])

no_of_words = 1
sentence = []


def findif(pseudo_sentence):
    words = pseudo_sentence
    for i in range(3, len(words)):
        if words[i].endswith(".") or words[i].endswith("?") or words[i].endswith("!"):
            return i
    return -1


for i in range(10):
    while True:
        first_word = random.choice(trigram_heads)
        if first_word[0].isupper() and not ("." in first_word[:-1] or "?" in first_word[:-1] or "!" in first_word[:-1]):
            break
    sentence.append(first_word)
    while True:
        population = list(set(trigram_dictionary[first_word]))
        weights = []
        for tail in dict3[first_word]:
            weights.append(dict3[first_word][tail])
        second_word = random.choices(population, weights)
        if no_of_words >= 5:
            if sentence[-1].endswith(".") or sentence[-1].endswith("!") or sentence[-1].endswith("?"):
                break
        first = str.split(first_word, " ")
        sentence.append(second_word[0])
        first_word = first[1] + " " + second_word[0]
        no_of_words += 1

    index = findif(sentence)
    sentence = sentence[:index+1]
    print(' '.join(sentence))
    no_of_words = 0
    sentence.clear()




