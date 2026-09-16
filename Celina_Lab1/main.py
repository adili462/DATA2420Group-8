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
        Date = values[1]
        Patient_Name = values[2]
        weight = float(values[3])
        height = float (values[4])
    except ValueError:
        raise TextFormatException()

    if height > 3:
        raise MeasurementUnitException
  
    return [exam_ID, Date, Patient_Name, weight, height]




def main():
    input_file=open("data.csv", "r")
    output_file=open("output.csv", "w")

    output_file.write("Exam ID,BMI\n")

    for row in input_file:
        try:
            L = parse_row(row)
            output_file.write(str(L[0])+","+str(compute_BMI(L[4],L[3]))+"\n")
        except TextFormatException:
            print(f"Exam {exam_ID}: Invalid text format.")
        except MeasurementUnitException:
            print(f"Exam {exam_ID}: Height should be in meters instead of feet.")
        except MissingValueException:
            print(f"Exam {exam_ID}: A value is missing.")


    input_file.close()
    output_file.close()



main()