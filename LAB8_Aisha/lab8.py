import pandas as pd


def task1_load_explore():
    """
    Task 1: load the labour.csv file and look at what is in it.
    :return: the DataFrame
    """
    df = pd.read_csv('labour.csv')

    # the column names in the file use - (wage-increase-first-year)
    # but the lab uses _ (wage_increase_first_year), so change every - to _
    new_names = []
    for name in df.columns:
        new_names.append(name.replace('-', '_'))
    df.columns = new_names

    print("First five rows:")
    print(df.head())
    print()

    print("Column names:")
    print(df.columns)
    print()

    print("Dimensions (rows, columns):")
    print(df.shape)
    print()

    print("Column data types:")
    print(df.dtypes)
    print()

    print("wage_increase_first_year column as a Series:")
    wage_first_year = df['wage_increase_first_year']
    print(wage_first_year)
    print()

    return df


def task2_access_data(df):
    """
    Task 2: get values out of the DataFrame using .loc[] and .iloc[]
    :param df: the DataFrame from task 1
    """
    # 1. one column is a Series
    wage_first_year = df['wage_increase_first_year']
    print("wage_increase_first_year Series:")
    print(wage_first_year)
    print()

    # 2. first value of the Series
    # .iloc[] uses the position (0 = first), .loc[] uses the row label (also 0 here)
    print("First value using .iloc[0]:", wage_first_year.iloc[0])
    print("First value using .loc[0]:", wage_first_year.loc[0])
    print()

    # 3. first five rows using .iloc[]
    print("First five rows using .iloc[0:5]:")
    print(df.iloc[0:5])
    print()

    # 4. two columns: use a list of column names
    print("wage_increase_first_year and wage_increase_second_year:")
    print(df[['wage_increase_first_year', 'wage_increase_second_year']])
    print()

    # 5. one value using .loc[row label, column name]
    print("Row 1, wage_increase_second_year using .loc:")
    print(df.loc[1, 'wage_increase_second_year'])
    print()

    # 6. many rows and columns
    # .loc uses labels and the end row IS included (0 to 4 = 5 rows)
    print("Rows 0 to 4, three columns using .loc:")
    print(df.loc[0:4, ['duration', 'wage_increase_first_year', 'class']])
    print()

    # .iloc uses positions and the end is NOT included (0 to 4 = 5 rows)
    print("Rows 0 to 4, first three columns using .iloc:")
    print(df.iloc[0:5, 0:3])
    print()


def task3_filter_data(df):
    """
    Task 3: filter the DataFrame with Boolean conditions and do some math
    :param df: the DataFrame from task 1
    :return: dictionary with the counts, average and maximum
    """
    # 1. good outcome
    good = df[df['class'] == 'good']
    print("Disputes with a good outcome:", len(good))

    # 2. bad outcome
    bad = df[df['class'] == 'bad']
    print("Disputes with a bad outcome:", len(bad))

    # 3. first year wage increase more than 2.5
    high_wage = df[df['wage_increase_first_year'] > 2.5]
    print("Disputes with wage_increase_first_year > 2.5:", len(high_wage))

    # 4. more than 10 statutory holidays
    many_holidays = df[df['statutory_holidays'] > 10]
    print("Disputes with statutory_holidays > 10:", len(many_holidays))

    # 5. both conditions: use & and put each condition in brackets
    both = df[(df['wage_increase_first_year'] > 2.5) & (df['statutory_holidays'] > 10)]
    print("Disputes with both conditions:", len(both))
    print(both[['wage_increase_first_year', 'statutory_holidays', 'class']])
    print()

    # 6. average (mean skips missing values)
    average_wage = df['wage_increase_first_year'].mean()
    print("Average wage_increase_first_year:", average_wage)

    # 7. maximum
    max_wage = df['wage_increase_first_year'].max()
    print("Maximum wage_increase_first_year:", max_wage)
    print()

    results = {}
    results['good'] = len(good)
    results['bad'] = len(bad)
    results['high_wage'] = len(high_wage)
    results['many_holidays'] = len(many_holidays)
    results['both'] = len(both)
    results['average_wage'] = average_wage
    results['max_wage'] = max_wage
    return results


def main():
    df = task1_load_explore()
    task2_access_data(df)
    task3_filter_data(df)


if __name__ == "__main__":
    main()
