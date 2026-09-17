# this line imports some custom exceptions for use in this lab
# raise/handle them just like Exception, ValueError, or any other type of exception
from exceptions import TextFormatException, MissingValueException, MeasurementUnitException
import csv

def compute_BMI(height: float, weight: float) -> float:
    """
    compute body-mass-index:  weight / (mass**2)
    :param height: height in meters
    :param weight: weight in kg
    :return: BMI in kg/m**2
    """
    BMI = weight / mass ** 2
    return BMI

def parse_row(row: str) -> list:
    """
    Accepts a single row (string) read from the data file.
    Splits it into a list of individual values, cast to numeric datatypes where appropriate.
    :param row: the string row read from the file
    :return: the parsed row, as a list
    """
    values = row.strip().split(",") #split the row into values
    
    try:
        exam_ID = int(values[0])
        date = values[1]
        patient_name = values[2]
        weight = float(values[3])
        height = float(values[4])
    except ValueError:
        raise TextFormatException()
        
    if height > 3: # nobody is 3m tall
        raise MeasurementUnitException
    
    return [exam_ID, date, pateint_name, weight, height]

def main():
    input_file = open("data.csv", "r")
    output_file = open("output.csv", "w")
    output_file.write("Exam ID, BMI\n") 
    input_file.readline() #skipping header
    
    for row in input_file:
        exam_id = row.split(",")[0]
    
        try:
            values = parse_row(row)
            exam_ID = values[0]
            weight = values[3]
            height = values[4]
            bmi = compute_BMI(height, weight)
            output_file.write(f"{exam_ID},{bmi:.2f}\n")
        except TextFormatException:
            print(f"Exam {exam_id}: Invalid text format.")
        except MeasurementUnitException:
            print(f"Exam {exam_id}: Height entered in wrong unit.")
        except MissingValueException:
            print(f"Exam {exam_id}: Missing a value.")

    input_file.close()
    output_file.close()

main()
