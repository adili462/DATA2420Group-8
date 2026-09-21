# this file is used to read and write data

def strip_punctuation(word: str) -> str:
    """Remove punctuation from a word."""
    return ''.join(char for char in word if char.isalnum())

def load_data(file_name: str, data_format: str):
    """Load words from a newline-delimited text file."""
    if data_format == 'txt':
        # check separator between words (' ' or '\n')
        with open(file_name, 'r') as file:
            # return a set of non-empty words
            line1 = next(file)  # read the first line to check for separator
            if line1.strip() == '':
                raise ValueError("Error, the file is empty")
            elif not (' ' in line1):
                # if the first line does not contain spaces, assume words are separated by newlines
                return {line1.strip()} | {word.strip() for word in file if word.strip()}
            else:
                file.seek(0)  # reset file pointer to the beginning of the file
                for line in file:
                    if line.strip():  # skip empty lines
                        # create list of lower-case words without punctuation and whitespace
                        words = [strip_punctuation(word).strip().lower() for word in line.split(' ') if word.strip()]
                        return words
                # remove line1 part
                # if the first line contains spaces, assume words are separated by spaces
                #return [word.strip() for word in line1.split(' ') if word.strip()] + [word.strip() for word in file if word.strip()]
    else:
        raise ValueError("Error, data must be in valid TXT format")