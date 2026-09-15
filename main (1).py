# this line imports some custom exceptions for use in this lab
# raise/handle them just like Exception, ValueError, or any other type of exception
from exceptions import TextFormatException, MissingValueException, MeasurementUnitException


def compute_BMI(height: float, weight: float) -> float:
    """
    compute body-mass-index:  weight / (mass**2)
    :param height: height in meters
    :param weight: weight in kg
    :return: BMI in kg/m**2
    """
    raise NotImplementedError("you need to write this function")


def parse_row(row: str) -> list:
    """
    Accepts a single row (string) read from the data file.
    Splits it into a list of individual values, cast to numeric datatypes where appropriate.
    :param row: the string row read from the file
    :return: the parsed row, as a list
    """
    raise NotImplementedError("you need to write this function")


def main():
    
    # your code here


main()