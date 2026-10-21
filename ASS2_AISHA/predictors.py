from abc import ABC, abstractmethod
import math

from exceptions import OutOfSampleError


class Predictor(ABC):
    # ABC means this is an abstract class:
    # you can't make a Predictor object, only objects of the classes below it

    def __init__(self, historical_data):
        """
        Store historical DataTable.
        Also save the min and max of every feature, so new patients can be checked.
        :param historical_data: DataTable with the historical patients
        """
        self.historical_data = historical_data

        # the features are every column except TumorType
        self.feature_names = []
        for col_name in historical_data.get_column_names():
            if col_name != 'TumorType':
                self.feature_names.append(col_name)

        # dictionaries where key = feature name and value = min or max of that feature
        self.feature_mins = {}
        self.feature_maxs = {}
        for feature in self.feature_names:
            self.feature_mins[feature] = historical_data.get_column_min(feature)
            self.feature_maxs[feature] = historical_data.get_column_max(feature)

    def check_in_sample(self, patient: dict) -> None:
        """
        Raises OutOfSampleError if any feature of the patient is
        less than the historical min or greater than the historical max.
        :param patient: dict {column name: value} for one new patient
        """
        for feature in self.feature_names:
            value = patient[feature]
            smallest = self.feature_mins[feature]
            biggest = self.feature_maxs[feature]

            if value != None:   # a missing value can't be checked
                if value < smallest or value > biggest:
                    raise OutOfSampleError(
                        f"{feature} with value {value} is outside historical range [{smallest}, {biggest}]"
                    )

    @abstractmethod
    def predict(self, patient: dict) -> int:
        """
        Make a prediction for one patient.
        Each class below Predictor writes its own version of this method.
        """
        pass


class MajorityClassPredictor(Predictor):

    def __init__(self, historical_data):
        # super().__init__ runs the __init__ of Predictor (the parent class)
        super().__init__(historical_data)
        self.majority_class = None

        # count how many times each TumorType shows up
        # key = tumor type, value = count
        counts = {}
        for tumor_type in historical_data.get_column('TumorType'):
            if tumor_type not in counts:
                counts[tumor_type] = 0
            counts[tumor_type] += 1

        # find the tumor type with the biggest count
        biggest_count = 0
        for tumor_type in counts:
            if counts[tumor_type] > biggest_count:
                biggest_count = counts[tumor_type]
                self.majority_class = int(tumor_type)

    def predict(self, patient: dict) -> int:
        """
        Always return the most common historical TumorType.
        :param patient: dict {column name: value} for one new patient
        :return: 0 (benign) or 1 (malignant)
        """
        self.check_in_sample(patient)
        return self.majority_class


class NearestNeighborPredictor(Predictor):

    def __init__(self, historical_data):
        # super().__init__ runs the __init__ of Predictor (the parent class)
        super().__init__(historical_data)

    def distance(self, patient1: dict, patient2: dict) -> float:
        """
        Calculate Euclidean distance using Feature1-Feature9 only.
        If either patient is missing a feature (None), that feature is skipped.
        :return: the distance between the two patients
        """
        total = 0
        for feature in self.feature_names:   # TumorType is not in feature_names
            value1 = patient1[feature]
            value2 = patient2[feature]

            if value1 != None and value2 != None:
                difference = value1 - value2
                total += difference ** 2

        return math.sqrt(total)

    def predict(self, patient: dict) -> int:
        """
        Find closest historical patient and return its TumorType.
        :param patient: dict {column name: value} for one new patient
        :return: 0 (benign) or 1 (malignant)
        """
        self.check_in_sample(patient)

        closest_distance = None
        closest_tumor_type = None

        for i in range(len(self.historical_data.data)):
            historical_patient = self.historical_data.get_row(i)
            dist = self.distance(patient, historical_patient)

            if closest_distance == None or dist < closest_distance:
                closest_distance = dist
                closest_tumor_type = historical_patient['TumorType']

        return int(closest_tumor_type)
