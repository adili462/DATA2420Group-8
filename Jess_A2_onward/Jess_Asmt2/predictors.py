from abc import ABC, abstractmethod
import math
import data_representation
from exceptions import OutOfSampleError


class Predictor(ABC):

    def __init__(self, historical_data):
        """
        Store historical DataTable.
        """
        self.historical_data = historical_data

    @abstractmethod
    def predict(self, patient):
        """
        Make a prediction for one patient.
        """
        pass


class MajorityClassPredictor(Predictor):

    def __init__(self, historical_data):
        super().__init__(historical_data)
        # TODO: calculate most common TumorType
        avg_type = historical_data.get_column_average("TumorType")
        self.majority_class = round(avg_type)


    def predict(self, patient):
        """
        Always return the most common historical TumorType.
        """
        return self.majority_class


class NearestNeighborPredictor(Predictor):

    def __init__(self, historical_data):
        super().__init__(historical_data)

        # list of feature names to iterate thru for
        # calculating Euclidean distance, excluding TumorType
        self.feature_names = [
            name
            for name in historical_data.get_column_names()
            if name != "TumorType"
        ]

        # historical range of each feature
        self.feature_ranges = {
            feature: (
                historical_data.get_column_min(feature),
                historical_data.get_column_max(feature),
            )
            for feature in self.feature_names
        }

    def distance(self, new_patient, hist_patient, col_names, min_hist, max_hist):
        """
        Calculate Euclidean distance using Feature1-Feature9 only, for one pair of patients.
        """
        # col_names = ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5", "Feature6",
        #              "Feature7", "Feature8", "Feature9"]
        
        # square sum, looping thru Features
        sq_sum_list = []
        for feat in col_names: # current feature as string column name
            p1_feat = new_patient[feat]
            p2_feat = hist_patient[feat]
            # check if feat is out of historical range
            # pass min and max from predict fn
            #min_hist, max_hist = self.feature_ranges[feat]

            if p1_feat > max_hist or p1_feat < min_hist:
                raise OutOfSampleError(
                    f"A {feat} value of {p1_feat} is outside the historical"
                    f"range, {min_hist} to {max_hist}, for patient row {new_patient}"
                )
            # calculate
            sqdiff = (p1_feat - p2_feat)**2
            sq_sum_list.append(sqdiff)
        # square root over sum
        return math.sqrt(sum(sq_sum_list))

    def predict(self, patient, col_names, min_hist, max_hist):
        """
        Find closest historical patient and return its TumorType.
        """
        # patient = the new patient

        # loop thru historical, calc Eu dist from patient to each row
        eu_dist_list = []
        for hist_patient in self.historical_data:
            eudist = self.distance(patient, hist_patient, col_names, min_hist, max_hist)
            eu_dist_list.append(eudist) # store eu dists in ordered list

        # find minimum eu in ordered list
        min_eu = min(eu_dist_list)
        # return TumorType from this patient index ^
        min_eu_index = eu_dist_list.index(min_eu)
        new_tumor_type = self.historical_data.get_row(min_eu_index)["TumorType"]
        return new_tumor_type