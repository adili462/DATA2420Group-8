from classes import Team, Driver


def load_teams(filename: str) -> dict:
    teams = {}

    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    # lines[1:] skips the header line (Driver,Team,Points)
    for line in lines[1:]:
        line = line.strip()
        if line == '':
            continue   # skip blank lines

        try:
            driver_name, team_name, points = line.split(',')
            points = int(points)
        except ValueError:
            print('Skipping bad line:', line)
            continue

        # each team appears many times in the file: only neeed to create ONE Team object for it
        if team_name not in teams:
            teams[team_name] = Team(team_name)

        teams[team_name].add_driver(Driver(driver_name, points))

    return teams


# this "if" makes the code below run only when main.py itself is run,
# not when the notebook imports load_teams from this file
if __name__ == '__main__':

    # Task 2 - load the driver and team information
    teams = load_teams('f1_points.csv')
    print('Number of teams:', len(teams))

    # Task 3 - sort the Teams by number of points
    # sorted() compares the Team objects to each other using their __lt__ method
    sorted_teams = sorted(teams.values())

    print()
    print('Teams sorted from least points to most points:')
    for team in sorted_teams:
        print(team)
