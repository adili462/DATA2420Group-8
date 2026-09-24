
# Step 1: Read data from files
import string  # ready-made string of all punctuation marks

# if the filenames change, we only need to edit them in one place.
STOPWORDS_FILE = './Lab2_combine/data/stopwords.txt'
TEXT_FILES = ['./Lab2_combine/data/textA.txt', './Lab2_combine/data/textB.txt']

# Step 1: Read data from files
def read_file_as_text(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text


def split_into_raw_words(text):
    raw_words = text.split()
    return raw_words


def clean_word(word):
    # removes punctuation in the beginning or end of word
    stripped = word.strip(string.punctuation)
    cleaned = stripped.lower()
    return cleaned


def clean_word_list(raw_words):
    cleaned_words = []
    for raw_word in raw_words:
        cleaned_words.append(clean_word(raw_word))
    return cleaned_words


def build_stopword_set(words):
    # hashing is faster than scanning through a list one item at a time
    stopword_set = set()
    for word in words:
        stopword_set.add(word)
    return stopword_set


def load_stopwords(filename):
    #returns as a set of clean words
    text = read_file_as_text(filename)
    raw_words = split_into_raw_words(text)
    cleaned_words = clean_word_list(raw_words)
    return build_stopword_set(cleaned_words)


def is_valid_word(word, stopwords):
    # blanks are thrown out as well
    if word == '':
        return False
    if word in stopwords:
        return False
    return True


def filter_words(words, stopwords):
    filtered = []
    for word in words:
        if is_valid_word(word, stopwords):
            filtered.append(word)
    return filtered


def load_words(filename, stopwords):
    # reading file and returning all words excluding stop words
    text = read_file_as_text(filename)
    raw_words = split_into_raw_words(text)
    cleaned_words = clean_word_list(raw_words)
    return filter_words(cleaned_words, stopwords)

# Step 2: Calculate term frequencies

# Step 3: Reduce to unique words

# tie Step 1, 2, and 3 together


def main():
    # Step 1: read the files
    # Step 2: calculate term frequencies
    # Step 3: reduce to unique words
    return

if __name__ == '__main__':
    main()