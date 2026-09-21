from file_IO import load_from_html, load_from_csv
from data_processing import print_stats

"""
    What main6.py does before edits:
    Loads a dataset from student_dataset.txt (HTML)
    and prints statistics about the dataset."""

def check_data_format(file_name: str) -> str:
    """
    checks the data format of the dataset in student_dataset.txt
    :return: 'html' if the dataset is in HTML format, 'csv' if it is in CSV format,
    or raise an exception if it is neither
    """
    #file = './Asmt1/Data/student_dataset.txt'
    with open(file_name, 'r') as file:
        header = file.read()
        if '<table>' in header and '</table>' in header:
            return 'html'
        elif ',' in header:
            return 'csv'
        else:
            raise ValueError("Error, data must be in valid CSV or HTML format")

# load data
filename = './Asmt1/Data/student_dataset.txt'
data_format = check_data_format(filename)

if data_format == 'html':
    table = load_from_html(filename)
elif data_format == 'csv':
    #print("CSV format detected, but load_from_csv is not yet implemented.")
    table = load_from_csv(filename)

# print table statistics
print_stats(table)