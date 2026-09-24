
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
def count_words(words):
    # how many times a word shows up
    counts = {}
    for word in words:
        # if we've seen this word already, add 1 to its existing count
        if word in counts:
            counts[word] += 1
        # start count at 1
        else:
            counts[word] = 1
    return counts


def total_word_count(counts):
    return sum(counts.values())


def calculate_term_frequency(count, total_words):
    if total_words == 0:
        raise ValueError('cannot compute term frequency: document has no words')
        # edge case: if file is empty due to all stop words
    return count / total_words


def term_frequencies(counts):
    # document's total word count once
    total_words = total_word_count(counts)

    # check this BEFORE the loop, since if counts is empty, the loop runs zero times 
    if total_words == 0:
        raise ValueError('cannot compute term frequencies: document has no words')

    # this dict will map word (its term frequency score)
    frequencies = {}
    for word, count in counts.items():
        frequencies[word] = calculate_term_frequency(count, total_words)
    return frequencies

# Step 3: Reduce to unique words
def find_common_words(dict_a, dict_b):
    # .keys() gives us each dict's words, wrapping in set(), return the words found in BOTH sets
    keys_a = set(dict_a.keys())
    keys_b = set(dict_b.keys())
    return keys_a & keys_b


def remove_words(dictionary, words_to_remove):
    # start with a fresh empty dict, copy over the wordpairs NOT in words_to_remove
    reduced_dict = {}
    for word, value in dictionary.items():
        if word not in words_to_remove:
            reduced_dict[word] = value
    return reduced_dict


def reduce_to_unique_words(dict_a, dict_b):
    # find which words the two documents share, remove then leave unique words
    common_words = find_common_words(dict_a, dict_b)
    unique_a = remove_words(dict_a, common_words)
    unique_b = remove_words(dict_b, common_words)
    return unique_a, unique_b, common_words

# tie Step 1, 2, and 3 together
def run_step_1(text_files, stopwords_file):
    # read the stopwords and both text files, return their word lists
    stopwords = load_stopwords(stopwords_file)
    words_doc1 = load_words(text_files[0], stopwords)
    words_doc2 = load_words(text_files[1], stopwords)
    return words_doc1, words_doc2

def run_step_2(words_doc1, words_doc2):
    # turn each word list into a term-frequency dict
    counts_doc1 = count_words(words_doc1)
    counts_doc2 = count_words(words_doc2)

    freq_doc1 = term_frequencies(counts_doc1)
    freq_doc2 = term_frequencies(counts_doc2)
    return freq_doc1, freq_doc2

def run_step_3(freq_doc1, freq_doc2):
    unique_doc1, unique_doc2, common_words = reduce_to_unique_words(freq_doc1, freq_doc2)
    return unique_doc1, unique_doc2, common_words

def print_results(text_files, unique_doc1, unique_doc2, common_words):
    print(f'Words common to both documents ({len(common_words)}):')
    print(common_words)

    print(f'\nUnique term frequencies for {text_files[0]}:')
    print(unique_doc1)

    print(f'\nUnique term frequencies for {text_files[1]}:')
    print(unique_doc2)

def main():
    # Step 1: read the files
    words_doc1, words_doc2 = run_step_1(TEXT_FILES, STOPWORDS_FILE)
        
    # Step 2: calculate term frequencies
    freq_doc1, freq_doc2 = run_step_2(words_doc1, words_doc2)

    # Step 3: reduce to unique words
    unique_doc1, unique_doc2, common_words = run_step_3(freq_doc1, freq_doc2)
    
    print_results(TEXT_FILES, unique_doc1, unique_doc2, common_words)

if __name__ == '__main__':
    main()
