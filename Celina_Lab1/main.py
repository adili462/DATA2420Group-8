# this line imports some custom exceptions for use in this lab
# raise/handle them just like Exception, ValueError, or any other type of exception
from exceptions import TextFormatException, MissingValueException, MeasurementUnitException


def compute_BMI(height: float, weight: float) -> float:
    """
    compute body-mass-index:  weight / (height**2)
    :param height: height in meters
    :param weight: weight in kg
    :return: BMI in kg/m**2
    """
    BMI = round(weight / (height**2),2)
    return BMI


def parse_row(row: str) -> list:
    """
    Accepts a single row (string) read from the data file.
    Splits it into a list of individual values, cast to numeric datatypes where appropriate.
    :param row: the string row read from the file
    :return: the parsed row, as a list
    """
    values = row.strip().split(",")



    try:
        exam_ID = int(values[0])

        if len(values) != 5:
                raise MissingValueException(f"Exam no. {exam_ID}: A value is missing.")
        
        Date = values[1]
        Patient_Name = values[2]
        weight = float(values[3])
        height = float (values[4])

    except ValueError:
        raise TextFormatException(f"Exam no. {exam_ID}: Invalid text format.")

    if height > 3:
        raise MeasurementUnitException(f"Exam no. {exam_ID}: A value is in the wrong units.")
    if weight > 90:
        raise MeasurementUnitException(f"Exam no. {exam_ID}: A value is in the wrong units.")

    if not(" " in Patient_Name):
        raise TextFormatException(f"Exam no. {exam_ID}: Patient name formatted incorrectly.")
    if not("/" in Date):
        raise TextFormatException(f"Exam no. {exam_ID}: Date formatted incorrectly.")

    
    check_Date = Date.split("/")
    for x in range(len(check_Date)):
        check_Date[x] = float(check_Date[x])
    if len(check_Date) != 3:
        raise TextFormatException(f"Exam no. {exam_ID}: Date formatted incorrectly.")
    if 1 > check_Date[0] or check_Date[0] >12:
        raise TextFormatException(f"Exam no. {exam_ID}: Date formatted incorrectly.")
    if 1 > check_Date[1] or check_Date[1]>31:
        raise TextFormatException(f"Exam no. {exam_ID}: Date formatted incorrectly.")
    if 2000 > check_Date[2] or check_Date[2]>2026:
        raise TextFormatException(f"Exam no. {exam_ID}: Date formatted incorrectly.")

    
    
    return [exam_ID, Date, Patient_Name, weight, height]




def main():
    input_file=open("data.csv", "r")
    output_file=open("output.csv", "w")

    output_file.write("Exam ID,BMI\n")

    next(input_file) #skips header from input_file

    for row in input_file:
        try:
            L = parse_row(row)
            output_file.write(str(L[0])+","+str(compute_BMI(L[4],L[3]))+"\n")
        except TextFormatException as tfe:
            print(tfe)
        except MeasurementUnitException as mue:
            print(mue)
        except MissingValueException as mve:
            print(mve)


    input_file.close()
    output_file.close()

#edge cases
#row = [17,10/9/2002, Zephyr Crael,79,1.55]

main()