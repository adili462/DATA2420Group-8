from exceptions import TextFormatException, MissingValueException, MeasurementUnitException
from classes import PatientExam
from pathlib import Path
import csv

def parse_month(mon: int) -> str:
    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    mon_str = month_names[mon-1]
    return mon_str

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

    r_items[0] = int(eID) # type: ignore # exam ID -> int
    eID_int = r_items[0] # store int version of exam ID for exception message

    if not weight_kg.strip():
        raise MissingValueException(f"Missing value for weight, Exam ID {eID_int}")

    if not weight_kg.isdigit(): # if weight is not an integer string, raise format error
        raise TextFormatException(f"Invalid weight format for Exam ID {eID_int}: is float, expected int")
    r_items[3] = int(weight_kg) # pyright: ignore[reportArgumentType] # if weight not missing, convert to int

    if not height_m.strip():
        raise MissingValueException(f"Missing value for height, Exam ID {eID_int}")
    r_items[4] = float(height_m) # pyright: ignore[reportArgumentType] # if height not missing, convert to float

    if r_items[4] > 3.0: # if height is greater than 3 meters, raise MeasurementUnitException
        raise MeasurementUnitException(f"Invalid measurement unit for height, Exam ID {eID_int}")

    return r_items


def main():
    ''' * modified from Lab 1 *
    Using the PatientExam class, main() parses each row of CSV file into a PatientExam object.
    Task 2: Creates list of PatientExam objects from CSV file.
    Task 3: Computes average BMI across all patients and busiest exam month for the clinic.
    '''
    data_file = Path(__file__).parent / 'data' / 'patient_data.csv'
    with open(data_file, newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        header = next(datareader) # removes header
        all_patients = [] # list to hold PatientExam objects
        all_bmi = [] # list to hold BMI values for all patients
        exam_months_count = { # dict to hold exam months for all patients
            1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0
        }

        for row in datareader:
            try:
                # parse row into list of items, and convert to numeric types where appropriate
                r_list = parse_row(','.join(row))

                # instantiates a PatientExam object with the parsed data
                # attributes in order: exam_id (int), date, name, weight (int), height (float)
                new_patient = PatientExam(r_list[0], r_list[1], r_list[2], r_list[3], r_list[4])
                all_patients.append(new_patient)
                all_bmi.append(new_patient.get_BMI())
                month = new_patient.get_exam_month()
                exam_months_count[month] += 1

            except MissingValueException as mve:
                print(mve)
            except MeasurementUnitException as mue:
                print(mue)
            except TextFormatException as tfe:
                print(tfe)
        
        avg_bmi = sum(all_bmi) / len(all_bmi)
        max_month = max(exam_months_count, key=exam_months_count.get) # type: ignore
        print("The average BMI across all patients is: ", avg_bmi)
        print("The busiest month for the clinic was: ", parse_month(max_month))
        patient_list_print_yn = input("Would you like to print the list of all patient objects?" \
        "Enter y to print, any other input will end program.")
        if patient_list_print_yn == 'y':
            print("List of all patient objects: \n", all_patients)


main()
print("Thank you for trying out our program. End of script.")