

def process_file(input_file):
    text_file = open(input_file,"r")
    text_lst = []
    for line in text_file:
        hold = line.strip().split(" ")
        text_lst=+ hold
    return text_lst



## removes any punctuation
def strip_punctuation(word:str)->str:
    new_word = ""
    for char in word:
        if char.isalnum():
            new_word += char
    return new_word


def build_dict(L:list)->dict:
    dictionary = dict()
    for word in L:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] = dict.get(word) + 1
    return dictionary



def main():
    #opens stopword text file
    stopword_file = open("./Celina_Lab2/stopwords.txt","r")

    #creates set of stopwords in "stopwordset"
    stopword_set = set()
    for x in stopword_file:
        stopword_set.add(x.strip().lower())

    textA = process_file("./Celina_Lab2/TextA.txt")
    textB = process_file("./Celina_Lab2/TextB.txt")

    # removes any punctuation attached to any words in textA and textB
    for word in range(len(textA)):
        textA[word] = strip_punctuation(textA[word])
    for word in range(len(textB)):
        textB[word] = strip_punctuation(textB[word])

    ## removes stopwords from sets of textA and textB
    textA = set(textA) - stopword_set
    textB = set(textB) - stopword_set

  

    # run build_dict function
    textA_dict = build_dict(textA)
    textB_dict = build_dict(textB)

    # builds set of words common between the two text files
    common_words = set()

    for key in textA_dict:
        if key in textB_dict:
            common_words.add(key)

    print("The set of words present in dictionary A and dictionary B are: " + common_words)

    ## removes common words from both textA and textB dictionaries
    for key in textA_dict:
        if key in common_words:
            del textA_dict[key]

    for key in textB_dict:
        if key in common_words:
            del textA_dict[key]


main()