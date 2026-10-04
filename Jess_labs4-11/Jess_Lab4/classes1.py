
class Driver:

    def __init__(self, name: str, points: int):
        """
        :param name: the driver's name
        :param points: points scored by this driver
        """
        pass # your code here

    def __repr__(self) -> str:
        """
        This method defines what the human-readable string version of the Driver object is.
        It should return a string that describes this Driver. For example:
        "Carlos Sainz (200 pts)"
        """
        pass # your code here


class Team:

    def __init__(self, name: str):
        """
        :param name: the team's name
        """
        pass # your code here

    def add_driver(self, driver: Driver) -> None:
        """
        adds a Driver to this team (by appending it to self.drivers)
        :param driver: the Driver object to add to this Team
        """
        pass # your code here

    def get_total_points(self) -> int:
        """
        :return: sum of points scored by this team's Drivers
        """
        pass # your code here

    def __repr__(self) -> str:
        """
        This method defines what the human-readable string version of the Team object is.
        It should return a string that describes this Team, for example:
        "FERRARI with drivers Carlos Sainz, Charles Leclerc. Total pts: 406"
        """
        pass # your code here
    
    def __lt__(self, other) -> bool:
        """
        This method defines what "less than" means for the Team object
        It should return True if this Team (self) is "less than" another.
        In this case, it should return True if this team has less total points that the other.
        :param other: another Team object
        :return: True if this Team has less points than other
        """
        pass # your code here
