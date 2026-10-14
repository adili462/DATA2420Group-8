#!/usr/bin/env python
# coding: utf-8

# # Assignment 2 - DataTable class

# In[ ]:


class DataTable:
    def __init__(self, csv_path: str):
        
        file = open(csv_path, 'r')
        text = file.read()
        file.close()

        # split the text of the file into a list of lines
        lines = text.split('\n')

        # the first line of the file holds the column names
        self.column_names = lines[0].split(',')

        for line in lines[1:]:
            if line != '':   # ignore blank lines
                values = line.split(',')
                row = {}
                for i in range(len(self.column_names)):
                    try:
                        row[self.column_names[i]] = float(values[i])
                    except ValueError:
                        row[self.column_names[i]] = None   # missing value
                self.data.append(row)

    def get(self, row_idx: int, col_name: str):
        # Return a single value from a row and column.
        return self.data[row_idx][col_name]

    def get_column(self, col_name: str) -> list:
        # Return all values in a column.
        column = []
        for row in self.data:
            column.append(row[col_name])
        return column

    def get_row(self, row_idx: int) -> dict:
        # Return a row as {column_name: value}
        return self.data[row_idx]

    def get_column_names(self) -> list:
        # Return list of column names.
        return self.column_names

    def get_known_values(self, col_name: str) -> list:
        # Return the values in a column, leaving out missing (None) values.
        known = []
        for value in self.get_column(col_name):
            if value != None:
                known.append(value)
        return known

    def get_column_average(self, col_name: str) -> float:
        # Return average of a column.
        values = self.get_known_values(col_name)
        return sum(values) / len(values)

    def get_column_min(self, col_name: str) -> float:
        # Return minimum value of a column.
        return min(self.get_known_values(col_name))

    def get_column_max(self, col_name: str) -> float:
        # Return maximum value of a column.
        return max(self.get_known_values(col_name))

