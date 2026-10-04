from classes1 import Team, Driver
from pathlib import Path
from exceptions import MissingValueException
import csv

def parse_row(row: str) -> dict:
    """
    Accepts a single row (string) read from the data file.
    Splits it into a dict of individual values, cast to numeric datatypes where appropriate.
    :param row: the string row read from the file
    :return: the parsed row, as a dict
    """

    # check right # of items per row?

    # use .split() and ID numbers/replace in list later
    r_items = row.split(',') # list of strings for now

    if not row.strip():
        # detect missing values (empty strings) before attempting conversion
        raise MissingValueException(f"Missing value for Driver {r_items[0]}")

    keys = ["Driver", "Team", "Points"]
    values = row.strip().split(",")
    # convert points to int
    values[-1] = int(values[-1]) # type: ignore

    return dict(zip(keys, values)) # type: ignore # ignore error

def main():
    str_team_list = [] # list of Team objects as strings
    team_list = [] # list of Team objects

    # lists made for debugging
    drivers_list = []

    #print(parse_row("Alexander Albon,WILLIAMS MERCEDES,27"))
    # read from csv file
    data_file = Path(__file__).parent / 'f1_points.csv'
    with open(data_file, newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        header = next(datareader) # removes header
        
        for row in datareader:
            try:
                # parse row into list of dicts, and convert to numeric types where appropriate
                r_list = parse_row(','.join(row))

                # instantiates a Driver object for each row
                new_driver = Driver(r_list["Driver"],r_list["Points"])
                drivers_list.append(new_driver)

                # checks if the team exists; instantiates a Team object if not
                maybe_new_team_str = r_list["Team"]
                if maybe_new_team_str not in str_team_list:
                    cur_team = Team(maybe_new_team_str)
                    team_list.append(cur_team)
                    str_team_list.append(maybe_new_team_str)
                else:
                    cur_team_str = str_team_list.index(maybe_new_team_str)
                    cur_team = Team(cur_team_str)
                
                # adds the Driver to their Team
                cur_team.add_driver(new_driver) # type: ignore


            except MissingValueException as mve:
                print(mve)

    # sorting
    sort_team_list = sorted(team_list)
    print(sort_team_list)



    #################
    # testing classes
    '''
    a1_drv = Driver("Josef", 67)
    a2_drv = Driver("Yeti", 69)
    team_A = Team("The A-Team")
    print(a1_drv)

    # add drivers to A-Team
    team_A.add_driver(a1_drv)
    team_A.add_driver(a2_drv)'''

main()