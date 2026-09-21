from data_IO_Lab2 import load_data
#from frequencies_jess_dont_merge_main import create_frequency_dict

# create a set of stopwords from the stopwords.txt file
file_stopwords = './Jess_Lab2/stopwords.txt'
stopwords = load_data(file_stopwords, 'txt', {})
#print(f"Stopwords: {stopwords}")

# create lists of words from textA and textB, excluding stopwords
file_textA = './Jess_Lab2/textA.txt'
textA_words = load_data(file_textA, 'txt', stopwords)
file_textB = './Jess_Lab2/textB.txt'
textB_words = load_data(file_textB, 'txt', stopwords)
print(textA_words)
print(textB_words)

# this is working! but right now troubleshooting stopwords above ^
# create frequency dictionaries for textA and textB
#freq_dict_A = create_frequency_dict(textA_words)
#freq_dict_B = create_frequency_dict(textB_words)
#print(f"Frequency Dictionary A: {freq_dict_A}")
#print(f"Frequency Dictionary B: {freq_dict_B}")