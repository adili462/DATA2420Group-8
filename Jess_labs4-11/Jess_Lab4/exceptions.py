"""
Custom exception types for handling specific error conditions in the patient exam data processing.
From Lab 1, borrowing/reusing in Lab 4 for efficient error handling and reporting.
"""


class TextFormatException(Exception):
    pass

class MissingValueException(Exception):
    pass

class MeasurementUnitException(Exception):
    pass
