"""
Custom exception types for handling specific error conditions in the patient exam data processing.
From Lab 1, reusing in Lab 3 for efficient error handling and reporting.
"""


class TextFormatException(Exception):
    pass

class MissingValueException(Exception):
    pass

class MeasurementUnitException(Exception):
    pass
