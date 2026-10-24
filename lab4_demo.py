from classes import Driver, Team
import csv

#Test Case 1 -  normal case

teams = ()

input_file = open("f1_points.csv", "r")

for row in input_file:
    driver_name = row[0]
    team_name = row[1]
    points = int(row[2])

    if team_name not in teams:
        teams[team_name] = Team(team_name)

    driver = Driver(driver_name, points)
    teams[team_name].add_driver(driver)

print("Number of Teams:", len(teams))