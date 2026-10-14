#!/usr/bin/env python
# coding: utf-8

# # Assignment 2 - Predictor classes

# In[ ]:


from abc import ABC, abstractmethod
import math

# run the exceptions notebook so OutOfSampleError can be used here
get_ipython().run_line_magic('run', 'exceptions.ipynb')


# In[ ]:


class Predictor(ABC):

    def __init__(self, historical_data):
        self.historical_data = historical_data

        # the features are every column except the label (TumorType)
        self.feature_names = []
        for name in historical_data.get_column_names():
            if name != "TumorType":
                self.feature_names.append(name)

    def check_in_sample(self, patient):
        for feature in self.feature_names:
            value = patient[feature]

            # a missing value (None) cannot be compared, so it is not checked
            if value != None:
                lowest = self.historical_data.get_column_min(feature)
                highest = self.historical_data.get_column_max(feature)

                if value < lowest or value > highest:
                    message = f"{feature} with value {value} is outside historical range [{lowest}, {highest}]"
                    raise OutOfSampleError(message)

    @abstractmethod
    def predict(self, patient):
        pass


# In[ ]:


class MajorityClassPredictor(Predictor):

    def __init__(self, historical_data):
        super().__init__(historical_data)
        self.majority_class = None

        # count how many times each TumorType appears
        counts = {}
        for tumor_type in historical_data.get_column("TumorType"):
            if tumor_type not in counts:
                counts[tumor_type] = 0
            counts[tumor_type] += 1

        # the majority class is the TumorType with the highest count
        highest_count = 0
        for tumor_type in counts:
            if counts[tumor_type] > highest_count:
                highest_count = counts[tumor_type]
                self.majority_class = int(tumor_type)

    def predict(self, patient):
        self.check_in_sample(patient)
        return self.majority_class


# In[ ]:


class NearestNeighborPredictor(Predictor):

    def __init__(self, historical_data):
        super().__init__(historical_data)

    def distance(self, patient1, patient2):
        total = 0
        for feature in self.feature_names:
            value1 = patient1[feature]
            value2 = patient2[feature]
            # a missing value (None) cannot be compared, so that feature is left out
            if value1 != None and value2 != None:
                total += (value1 - value2) ** 2
        return math.sqrt(total)

    def predict(self, patient):
        self.check_in_sample(patient)

        closest_row = self.historical_data.get_row(0)
        closest_distance = self.distance(patient, closest_row)

        for i in range(1, len(self.historical_data.data)):
            row = self.historical_data.get_row(i)
            current_distance = self.distance(patient, row)
            if current_distance < closest_distance:
                closest_distance = current_distance
                closest_row = row

        return int(closest_row["TumorType"])

