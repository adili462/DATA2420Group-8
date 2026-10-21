# creates a dictionary where
# each word is associated with its frequency
# e.g. {'word1': 3, 'word2': 5, 'word3': 1}

'''
def create_frequency_dict(words: list) -> dict:
    """Create a frequency dictionary from a list of words."""
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict
'''

def create_term_frequency_dict(words: list) -> dict:
    """Create a term frequency dictionary from a list of words."""
    term_frequency_dict = {}
    total_words = len(words)
    for word in words:
        if word in term_frequency_dict:
            term_frequency_dict[word] += 1
        else:
            term_frequency_dict[word] = 1
    # convert counts to term frequencies
    for word in term_frequency_dict:
        term_frequency_dict[word] /= total_words
    return term_frequency_dict