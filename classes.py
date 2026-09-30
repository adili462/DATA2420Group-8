class PatientExam:
    def __init__(self, exam_id: int, date: str, name: str, weight: int, height: float):
        if weight <= 0:
            raise ValueError("weight must be positive")
        self.exam_id = exam_id
        self.date = date
        self.name = name
        self.weight = weight
        self.height = height
 
    def get_BMI(self) -> float:
        return self.weight / (self.height * self.height)    # height 0 -> ZeroDivisionError
 
    def get_exam_month(self) -> int:
        parts = self.date.split('-')                        # '2024-10-03' -> ['2024', '10', '03']
        return int(parts[1])                                # 'abc' -> IndexError
