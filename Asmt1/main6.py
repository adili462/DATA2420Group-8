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
            raise Exception("Error, data must be in valid CSV or HTML format")

def main():
    # load data
    filename = './Asmt1/Data/student_dataset.txt'
    #filename = './Asmt1/Data/test.arff'

    try:
        data_format = check_data_format(filename)
        if data_format == 'html':
            table = load_from_html(filename)
        elif data_format == 'csv':
            table = load_from_csv(filename)
    except Exception as e:
        print(e)
        return
    except AttributeError as ae:
        print(ae)
        return

    # print table statistics
    print_stats(table)

    '''Celina part'''
    # make list of dictionaries
    # write to JSON format

    '''jess part'''
    # process corrupted data

main()