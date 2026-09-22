# Step 1: Read data from files

import string

STOPWORDS_FILE = 'data/stopwords.txt'
TEXT_FILES = ['data/textA.txt', 'data/textB.txt']


def load_stopwords(filename):
    with open(filename, 'r') as f:
        raw_words = f.read().split()
    return set(word.lower() for word in raw_words)


def clean_word(word):
    return word.strip(string.punctuation).lower()


def load_words(filename, stopwords):
    with open(filename, 'r') as f:
        raw_words = f.read().split()

    words = []
    for raw_word in raw_words:
        word = clean_word(raw_word)
        if word and word not in stopwords:
            words.append(word)
    return words

# Step 2: 
