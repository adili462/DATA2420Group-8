class OutOfSampleError(Exception):
    """
    Raised when a new input contains feature values
    outside the historical min/max range.
    """
    pass

class MissingValueException(Exception):
    """
    Raised during parsing when a row has missing values.
    """
    pass