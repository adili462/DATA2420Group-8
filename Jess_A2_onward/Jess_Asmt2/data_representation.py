import csv
from exceptions import MissingValueException


class DataTable:
    """
    Stores 1 table of data, read from a CSV file.
    Example: a DataTable of historical cancer cases.
    """
    @staticmethod
    def _parse_row(row: str, col_names: list[str], hd_length: int) -> dict:
        """
        Accepts a single row (string) read from the data file.
        Splits it into a dict of individual values, cast to numeric datatypes.
        :param row: the string row read from the file
        :param col_names: keys from the header, used to create dict rows
        :param hd_length: length of the header
        :return: the parsed row, as a dict
        """
        # use .split() and ID numbers/replace in list later
        r_items = row.split(',') # list of strings for now

        ### catch exceptions
        if any(value.strip() == "" for value in r_items):
            raise MissingValueException(f"Missing value in row: {r_items}")
        # check if row is correct length
        if len(r_items) != hd_length: # row length != header length
            raise MissingValueException(f"Missing value in row: {r_items}")
        # detect missing values (empty strings) before attempting conversion
        if not row.strip():
            raise MissingValueException(f"Missing value in row: {r_items}")

        # convert r_items to list of floats
        # detect exceptional case: can't convert to float
        r_float_list = []
        for item in r_items:
            if not (item.isnumeric()):
                raise ValueError(f"Cannot convert {item} to float in row {r_items}")
            else:
                #print(item, "after col num", len(r_float_list), "row content: ", r_items)
                r_float_list.append(float(item))
        # convert r_float_list to dict with keys from header
        return dict(zip(col_names, r_float_list))

    def _load(self, csv_path: str):
        rows = []
        with open (csv_path, newline='') as csvfile:
            datareader = csv.reader(csvfile, delimiter=',')
            column_names = next(datareader) # stores header and removes from future processing
            hd_len = len(column_names) # stores length of header instead of computing for each new row

            for row in datareader:
                try:
                    # read rows into dicts
                    r_dict = DataTable._parse_row(','.join(row), column_names, hd_len)
                    rows.append(r_dict)
                except MissingValueException as mve:
                    print(mve)
                except ValueError as ve:
                    print(ve)
        return column_names, rows

    def __init__(self, csv_path: str):
        """
        Load CSV data into memory.
        Convert all values to float.
        :csv_path: path of the CSV file to be read
        """
        #self.csv_path = csv_path # need this?
        self._column_names, self._rows = self._load(csv_path)


    def get(self, row_idx: int, col_name: str):
        """
        Return a single value from a row and column.
        """
        row = self.get_row(row_idx)
        return {col_name: row[col_name]}[col_name]

    def get_row(self, row_idx: int) -> dict:
        """
        Return a row as {column_name: value}
        """
        return self._rows[row_idx]

    def get_column(self, col_name: str) -> list:
        """
        Return all values in a column.
        """
        return [self._rows[i][col_name] for i in range(len(self._rows))]

    def get_column_names(self) -> list:
        """
        Return list of column names.
        """
        return self._column_names

    def get_column_average(self, col_name: str) -> float:
        """
        Return average of a column.
        """
        col = self.get_column(col_name) # list
        return sum(col) / len(col)

    def get_column_min(self, col_name: str) -> float:
        """
        Return minimum value of a column.
        """
        col = self.get_column(col_name) # list
        return min(col)

    def get_column_max(self, col_name: str) -> float:
        """
        Return maximum value of a column.
        """
        col = self.get_column(col_name) # list
        return max(col)

    def __len__(self) -> int:
        """
        Return length (number of rows) of the DataTable.
        """
        return len(self._rows)

    def __iter__(self) -> iter:
        """
        Return an iterator over the rows of the DataTable.
        """
        return iter(self._rows)

    # def __getitem__(self, row_idx: int) -> dict:
    #     """
    #     Return a row using list-style indexing.
    #     """
    #     return self._rows[row_idx]
