
class PatientExam:

    def __init__(self, exam_id: int, date: str, name: str, weight: int, height: float):
        self.exam_id = exam_id
        self.date = date
        self.name = name
        self.weight = weight
        self.height = height

    def get_BMI(self) -> float:
        """Calculates and returns the BMI of the patient."""
        return self.weight / (self.height ** 2)

    def get_exam_month(self) -> int:
        """Returns the month of the exam date."""
        # Assuming date format is 'M/D/YYYY'
        first_slash_index = self.date.find('/')
        return int(self.date[:first_slash_index])

'''Example from python.org docs:'''
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name: str):
        self.name = name    # instance variable unique to each instance

    def add_trick(self, trick):
            self.tricks.append(trick)
'''
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
'''