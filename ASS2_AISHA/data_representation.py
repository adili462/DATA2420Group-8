class DataTable:

    def __init__(self, csv_path: str):
        """
        Load CSV data into memory.
        Convert all values to float.
        :param csv_path: name of the csv file to load
        """
        self.column_names = []   # list of the column names (from the header line)
        self.data = []           # list of rows, each row is a dict {column name: value}

        file = open(csv_path, 'r')
        text = file.read()
        file.close()

        # split the text of the file into a list of lines
        lines = text.split('\n')

        # the first line is the header with the column names
        self.column_names = lines[0].split(',')

        # lines[1:] skips the header line
        for line in lines[1:]:
            if line != '':   # ignore blank lines
                values = line.split(',')

                row = {}
                for i in range(len(self.column_names)):
                    col_name = self.column_names[i]
                    try:
                        row[col_name] = float(values[i])
                    except ValueError:
                        # some values in the data are '?' (missing value)
                        # '?' can't be turned into a float, so store None instead
                        row[col_name] = None

                self.data.append(row)

    def get(self, row_idx: int, col_name: str) -> float:
        """
        Return a single value from a row and column.
        :param row_idx: the row number (starts at 0)
        :param col_name: the name of the column
        :return: the value in that row and column
        """
        row = self.get_row(row_idx)

        if col_name not in self.column_names:
            raise ValueError(f"{col_name} is not a column in this table")

        return row[col_name]

    def get_column(self, col_name: str) -> list:
        """
        Return all values in a column.
        :param col_name: the name of the column
        :return: list with the value from every row in that column
        """
        if col_name not in self.column_names:
            raise ValueError(f"{col_name} is not a column in this table")

        column = []
        for row in self.data:
            column.append(row[col_name])
        return column

    def get_row(self, row_idx: int) -> dict:
        """
        Return a row as {column_name: value}
        :param row_idx: the row number (starts at 0)
        :return: dictionary for that row
        """
        if row_idx < 0 or row_idx >= len(self.data):
            raise IndexError(f"row {row_idx} does not exist, the table has {len(self.data)} rows")

        return self.data[row_idx]

    def get_column_names(self) -> list:
        """
        Return list of column names.
        """
        return self.column_names

    def get_column_average(self, col_name: str) -> float:
        """
        Return average of a column.
        Missing values (None) are not counted.
        :param col_name: the name of the column
        """
        column = self.get_column(col_name)

        total = 0
        count = 0
        for value in column:
            if value != None:   # skip missing values
                total += value
                count += 1

        return total / count

    def get_column_min(self, col_name: str) -> float:
        """
        Return minimum value of a column.
        Missing values (None) are not counted.
        :param col_name: the name of the column
        """
        column = self.get_column(col_name)

        smallest = None
        for value in column:
            if value != None:   # skip missing values
                if smallest == None or value < smallest:
                    smallest = value

        return smallest

    def get_column_max(self, col_name: str) -> float:
        """
        Return maximum value of a column.
        Missing values (None) are not counted.
        :param col_name: the name of the column
        """
        column = self.get_column(col_name)

        biggest = None
        for value in column:
            if value != None:   # skip missing values
                if biggest == None or value > biggest:
                    biggest = value

        return biggest
