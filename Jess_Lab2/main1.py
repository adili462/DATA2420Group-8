from data_IO_Lab2 import load_data
from frequencies_jess_dont_merge_main import create_term_frequency_dict#, create_frequency_dict

def shared_words(dict1: dict, dict2: dict) -> set:
    """Return a set of words that are shared between two dictionaries.
    Assuming the two dictionaries don't contain stopwords."""
    return set(dict1.keys()) & set(dict2.keys())

def main():
    'Step 1: Load stopwords, textA, and textB'
    # create a set of stopwords from the stopwords.txt file
    file_stopwords = './Jess_Lab2/stopwords.txt'
    stopwords = load_data(file_stopwords, 'txt', {})
    #print(f"Stopwords: {stopwords}")

    # create lists of words from textA and textB, excluding stopwords
    file_textA = './Jess_Lab2/textA.txt'
    textA_words = load_data(file_textA, 'txt', stopwords)
    file_textB = './Jess_Lab2/textB.txt'
    textB_words = load_data(file_textB, 'txt', stopwords)
    #print(textA_words)
    #print(textB_words)

    'step 2: Create frequency dictionaries and term frequency dictionaries for textA and textB'
    # create frequency dictionaries for textA and textB
    # freq_dict_A = create_frequency_dict(textA_words)
    # freq_dict_B = create_frequency_dict(textB_words)
    # print(f"Frequency Dictionary A: {freq_dict_A}")
    # print(f"Frequency Dictionary B: {freq_dict_B}")

    # create term frequency dictionaries for textA and textB
    term_freq_dict_A = create_term_frequency_dict(textA_words)
    term_freq_dict_B = create_term_frequency_dict(textB_words)
    print(f"Term Frequency Dictionary A: {term_freq_dict_A}")
    print(f"Term Frequency Dictionary B: {term_freq_dict_B}")

    'step 3: Find and remove shared words between textA and textB'
    # convert textA and textB lists to dictionaries?
    textA_dict = {word: 1 for word in textA_words}
    textB_dict = {word: 1 for word in textB_words}

    # find shared words between textA and textB
    shared = shared_words(textA_dict, textB_dict)
    print(f"Shared words between textA and textB: {shared}")

    # remove shared words from textA and textB
    textA_unique = {word for word in textA_words if word not in shared}
    textB_unique = {word for word in textB_words if word not in shared}
    print(f"Unique words in textA: {textA_unique}")
    print(f"Unique words in textB: {textB_unique}")

main()