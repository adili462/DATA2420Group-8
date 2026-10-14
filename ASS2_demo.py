#!/usr/bin/env python
# coding: utf-8

# # Assignment 2
# 
# Predicting if a tumor is benign (0) or malignant (1) using the historical data.

# In[ ]:


# run the main notebook (it also runs the other notebooks)
# so all the classes and functions can be used here
get_ipython().run_line_magic('run', 'main.ipynb')


# In[ ]:


# load the 3 data files
historical = DataTable("data/cancer_historical.csv")
new_cases = DataTable("data/cancer_new_cases.csv")
labels = DataTable("data/cancer_new_cases_labels.csv")

# should be 599, 100 and 100 rows
print(len(historical.data))
print(len(new_cases.data))
print(len(labels.data))


# ## Task 1 - DataTable
# 
# I made a small file (data/test_small.csv) so I can check the answers by hand.

# In[ ]:


file = open("data/test_small.csv", "r")
print(file.read())
file.close()


# In[ ]:


small = DataTable("data/test_small.csv")


# Normal tests. The expected answer is printed beside the actual one.

# In[ ]:


print("column names")
print("expected: ['Height', 'Weight', 'TumorType']")
print("actual:  ", small.get_column_names())


# In[ ]:


print("get row 0, Height")
print("expected: 1.5")
print("actual:  ", small.get(0, "Height"))


# In[ ]:


print("get_row 2")
print("expected: {'Height': 4.0, 'Weight': 30.0, 'TumorType': 0.0}")
print("actual:  ", small.get_row(2))


# In[ ]:


print("get_column Height")
print("expected: [1.5, 2.5, 4.0]")
print("actual:  ", small.get_column("Height"))


# In[ ]:


# min, max and average of Height
# average should be (1.5 + 2.5 + 4.0) / 3 = 2.67
print("min expected 1.5, actual:", small.get_column_min("Height"))
print("max expected 4.0, actual:", small.get_column_max("Height"))
print("average expected 2.67, actual:", small.get_column_average("Height"))


# In[ ]:


# values should be floats. the file has 10 so it should come back as 10.0
value = small.get(0, "Weight")
print(value)
print(type(value))


# **Special case** 
# 
# The cancer files have a ? in some rows where there is no measurement. float("?") gives a ValueError so I store None instead, and min, max and average skip the None values.
# 
# The Weight column in my test file is 10, ?, 30 so the average should be (10 + 30) / 2 = 20

# In[ ]:


# missing values
print(small.get_column("Weight"))
print("min:", small.get_column_min("Weight"))
print("max:", small.get_column_max("Weight"))
print("average:", small.get_column_average("Weight"))


# In[ ]:


# new case 18 in the real data has a ? for Feature6
print(new_cases.get_row(18))


# **Error cases**

# In[ ]:


# file that doesn't exist
try:
    DataTable("data/not_a_file.csv")
except FileNotFoundError as error:
    print("FileNotFoundError:", error)


# In[ ]:


# column that doesn't exist
try:
    small.get(0, "Age")
except KeyError as error:
    print("KeyError:", error)


# In[ ]:


# row that doesn't exist (the table only has 3 rows)
try:
    small.get_row(50)
except IndexError as error:
    print("IndexError:", error)


# Now the real data. Every feature should go from 1 to 10.

# In[ ]:


print(historical.get_column_names())

for name in historical.get_column_names():
    print(name, historical.get_column_min(name), historical.get_column_max(name), historical.get_column_average(name))


# ## Task 2 - Predictors

# In[ ]:


mode_predictor = MajorityClassPredictor(historical)
nn_predictor = NearestNeighborPredictor(historical)


# ### Mode predictor
# 
# First count the tumor types myself to see which one is the most common.

# In[ ]:


benign = 0
malignant = 0
for tumor_type in historical.get_column("TumorType"):
    if tumor_type == 0:
        benign += 1
    else:
        malignant += 1

print("benign:", benign)
print("malignant:", malignant)


# In[ ]:


# benign is more common so the majority class should be 0
print(mode_predictor.majority_class)


# In[ ]:


# it should predict 0 for every patient, even one with really high values
patient1 = new_cases.get_row(0)
patient2 = new_cases.get_row(13)

print(patient1)
print(mode_predictor.predict(patient1))
print(patient2)
print(mode_predictor.predict(patient2))


# ### Nearest neighbor predictor
# 
# Testing the distance method first with two patients I made up. They are different by 3 in Feature1 and by 4 in Feature2 and the same for the rest, so the distance should be sqrt(3^2 + 4^2) = 5

# In[ ]:


a = {"Feature1": 1.0, "Feature2": 1.0, "Feature3": 1.0, "Feature4": 1.0, "Feature5": 1.0,
     "Feature6": 1.0, "Feature7": 1.0, "Feature8": 1.0, "Feature9": 1.0}

b = {"Feature1": 4.0, "Feature2": 5.0, "Feature3": 1.0, "Feature4": 1.0, "Feature5": 1.0,
     "Feature6": 1.0, "Feature7": 1.0, "Feature8": 1.0, "Feature9": 1.0}

print(nn_predictor.distance(a, b))


# In[ ]:


# special case: distance from a patient to itself should be 0
print(nn_predictor.distance(a, a))


# In[ ]:


# special case: the TumorType should not be used in the distance
# adding a TumorType to b should still give 5
b["TumorType"] = 1.0
print(nn_predictor.distance(a, b))


# In[ ]:


# special case: missing value
# if Feature2 is missing, only the 3 from Feature1 is left so it should be 3
b["Feature2"] = None
print(nn_predictor.distance(a, b))


# Prediction: If we give a patient that is already in the historical data, the closest patient is itself, so it should give back that patient's TumorType.
# 
# Row 5 of the historical data is malignant (1) and row 0 is benign (0).

# In[ ]:


print(historical.get_row(5))
print("prediction:", nn_predictor.predict(historical.get_row(5)))

print(historical.get_row(0))
print("prediction:", nn_predictor.predict(historical.get_row(0)))


# In[ ]:


# two new patients. patient1 has low values and patient2 has mostly 10s
# so I expect 0 for patient1 and 1 for patient2
print("prediction:", nn_predictor.predict(patient1), "actual:", labels.get(0, "TumorType"))
print("prediction:", nn_predictor.predict(patient2), "actual:", labels.get(13, "TumorType"))


# In[ ]:


# special case: new case 18 has a missing value, it should still get a prediction
print("prediction:", nn_predictor.predict(new_cases.get_row(18)), "actual:", labels.get(18, "TumorType"))


# ## Task 3 - OutOfSampleError
# 
# All the features in the historical data go from 1 to 10. If a new patient has a value lower than the min or higher than the max, predict should raise OutOfSampleError.

# In[ ]:


# error case: Feature4 is 11 which is more than the max of 10
too_high = {"Feature1": 1.0, "Feature2": 1.0, "Feature3": 1.0, "Feature4": 11.0, "Feature5": 1.0,
            "Feature6": 1.0, "Feature7": 1.0, "Feature8": 1.0, "Feature9": 1.0}

try:
    nn_predictor.predict(too_high)
except OutOfSampleError as error:
    print("OutOfSampleError:", error)


# In[ ]:


# the mode predictor raises it too
try:
    mode_predictor.predict(too_high)
except OutOfSampleError as error:
    print("OutOfSampleError:", error)


# In[ ]:


# error case: Feature1 is 0.5 which is less than the min of 1
too_low = {"Feature1": 0.5, "Feature2": 1.0, "Feature3": 1.0, "Feature4": 1.0, "Feature5": 1.0,
           "Feature6": 1.0, "Feature7": 1.0, "Feature8": 1.0, "Feature9": 1.0}

try:
    nn_predictor.predict(too_low)
except OutOfSampleError as error:
    print("OutOfSampleError:", error)


# In[ ]:


# special case: values that are exactly the min (1) or exactly the max (10) are still ok
# so these should give a prediction and no error
all_ones = {"Feature1": 1.0, "Feature2": 1.0, "Feature3": 1.0, "Feature4": 1.0, "Feature5": 1.0,
            "Feature6": 1.0, "Feature7": 1.0, "Feature8": 1.0, "Feature9": 1.0}

all_tens = {"Feature1": 10.0, "Feature2": 10.0, "Feature3": 10.0, "Feature4": 10.0, "Feature5": 10.0,
            "Feature6": 10.0, "Feature7": 10.0, "Feature8": 10.0, "Feature9": 10.0}

print(nn_predictor.predict(all_ones))
print(nn_predictor.predict(all_tens))


# ## Task 4 - main program
# 
# Testing calculate_accuracy with small lists first.

# In[ ]:


# 3 out of 4 are the same so it should be 0.75
print(calculate_accuracy([1, 0, 1, 1], [1, 0, 0, 1]))


# In[ ]:


# all right = 1.0, all wrong = 0.0
print(calculate_accuracy([1, 0], [1, 0]))
print(calculate_accuracy([1, 1], [0, 0]))


# In[ ]:


# special case: empty lists, should give 0.0 and not a ZeroDivisionError
print(calculate_accuracy([], []))


# Running the main program

# In[ ]:


main()


# The mode predictor always says 0, so its accuracy should be the same as the number of new cases that are really 0. Checking that:

# In[ ]:


zeros = 0
for label in labels.get_column("TumorType"):
    if label == 0:
        zeros += 1

print(zeros, "out of", len(labels.data))


# In[ ]:


# first 10 new cases with both predictions and the real answer
for i in range(10):
    patient = new_cases.get_row(i)
    print(i, mode_predictor.predict(patient), nn_predictor.predict(patient), labels.get(i, "TumorType"))


# In[ ]:


# the cases nearest neighbor got wrong
for i in range(len(new_cases.data)):
    prediction = nn_predictor.predict(new_cases.get_row(i))
    if prediction != labels.get(i, "TumorType"):
        print("case", i, "predicted", prediction, "but was", labels.get(i, "TumorType"))


# Nearest neighbor got 96 out of 100 and the mode predictor got 79 out of 100, so nearest neighbor is a lot better.
