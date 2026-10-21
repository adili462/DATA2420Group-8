# this line imports some custom exceptions for use in this lab
# raise/handle them just like Exception, ValueError, or any other type of exception
from exceptions import TextFormatException, MissingValueException, MeasurementUnitException
import csv

def compute_BMI(height: float, weight: float) -> float:
    """
    compute body-mass-index:  weight / (height**2)
    :param height: height in meters
    :param weight: weight in kg
    :return: BMI in kg/m**2 rounded to 2 decimals
    """
    return round(weight / height**2, 2)

def parse_row(row: str) -> list:
    """
    Accepts a single row (string) read from the data file.
    Splits it into a list of individual values, cast to numeric datatypes where appropriate.
    :param row: the string row read from the file
    :return: the parsed row, as a list
    """
    # use .split() and ID numbers/replace in list later
    r_items = row.split(',') # list of strings for now

    # check if the row has the correct number of items

    if len(r_items) != 5:
        id_return = r_items[0]
        raise TextFormatException(f"Items for Exam ID {id_return} are wrongly formatted")

    # hard code indexes to convert to number types
    eID = r_items[0] # exam ID string
    weight_kg = r_items[3] # weight in kg, string
    height_m = r_items[4] # height in m, string

    # scan for exceptions
    if not eID.strip(): # detect missing values (empty strings) before attempting conversion
        raise MissingValueException(f"Missing value for Exam ID {r_items[0]}")
        #return ['Missing value in this row:', row] # edit return message, generic, only needed for length

    r_items[0] = int(eID) # exam ID -> int
    eID_int = r_items[0] # store int version of exam ID for exception message

    if not weight_kg.strip():
        raise MissingValueException(f"Missing value for Exam ID {eID_int}")
        #return ['Missing value in this row:', row]
    r_items[3] = float(weight_kg) # if weight not missing, convert to float

    if not height_m.strip():
        raise MissingValueException(f"Missing value for Exam ID {eID_int}")
        #return ['Missing value in this row:', row]
    r_items[4] = float(height_m) # if height not missing, convert to float

    if r_items[4] > 3.0: # if height is greater than 3 meters, raise MeasurementUnitException
        raise MeasurementUnitException(f"Invalid measurement unit for Exam ID {eID_int}")
        #return ['Invalid measurement unit in this row:', row]

    return r_items


def main():
    # step 1: read row from csv to string
    # -> master_string_list = list of each patient row stored as a string
    with open('data.csv', newline='') as csvfile:
        """
        read csv and output each row as a string item in a list
        :return: each row as a string item in input_string_list
        """
        datareader = csv.reader(csvfile, delimiter=',')
        header = next(datareader) # removes header
        master_string_list = []
        for row in datareader:
            master_string_list.append(','.join(row))

    # step 2: parse_row into list (Req1) and calc BMI
    final_list = []
    for r in master_string_list: # iterate through rows
        try:
            r_list = parse_row(r) # list of items in current row (tested, updates each itrn)
            if len(r_list) < 5: # if parse_row returned an error message, skip this row
                continue
            e_ID = r_list[0] # get ID, weight and height
            wt = r_list[3]
            ht = r_list[4]
            bmi = compute_BMI(ht,wt)
            new_tuple = (str(e_ID), str(bmi))
            final_list.append(new_tuple)
        except MissingValueException as mve:
            print(mve)
        except MeasurementUnitException as mue:
            print(mue)
        except TextFormatException as tfe:
            print(tfe)

    # set up new CSV for writing
    with open('output.csv', mode='w', newline='') as outfile:
        writer = csv.writer(outfile)

        # write header
        writer.writerow(['Exam ID', 'BMI'])

        # write all rows
        writer.writerows(final_list)
    return

main()