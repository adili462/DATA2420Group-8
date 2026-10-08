
class Driver:

    def __init__(self, name: str, points: int):
        """
        :param name: the driver's name
        :param points: points scored by this driver
        """
        self.name = name
        self.points = points

    def __repr__(self) -> str:
        """
        This method defines what the human-readable string version of the Driver object is.
        It should return a string that describes this Driver. For example:
        "Carlos Sainz (200 pts)"
        """
        return "" + self.name + " (" + str(self.points) + " pts)"

class Team:

    def __init__(self, name: str):
        """
        :param name: the team's name
        """
        self.name = name
        self.drivers = []

    def add_driver(self, driver: Driver) -> None:
        """
        adds a Driver to this team (by appending it to self.drivers)
        :param driver: the Driver object to add to this Team
        """
        self.drivers.append(driver)

    def get_total_points(self) -> int:
        """
        :return: sum of points scored by this team's Drivers
        """
        total_pts = 0
        for driver in self.drivers:
            total_pts += driver.points
        return total_pts

    def __repr__(self) -> str:
        """
        This method defines what the human-readable string version of the Team object is.
        It should return a string that describes this Team, for example:
        "FERRARI with drivers Carlos Sainz, Charles Leclerc. Total pts: 406"
        """
        dr_string = ""
        for driver in self.drivers:
            if self.drivers[-1] == driver: # if we're on the last driver
                dr_string += driver.name + "."
            else: # if we have more drivers to add, add a comma
                dr_string += driver.name + ", "
        return "" + self.name + " with drivers " + dr_string + " Total pts: " + str(self.get_total_points())
    
    def __lt__(self, other) -> bool:
        """
        This method defines what "less than" means for the Team object
        It should return True if this Team (self) is "less than" another.
        In this case, it should return True if this team has less total points that the other.
        :param other: another Team object
        :return: True if this Team has less points than other
        """
        if self.get_total_points() < other.get_total_points():
            return True
        else:
            return False
