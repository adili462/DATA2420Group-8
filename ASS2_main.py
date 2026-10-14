#!/usr/bin/env python
# coding: utf-8

# # Assignment 2 - main program

# In[ ]:


# run the other notebooks so DataTable, the predictors and OutOfSampleError can be used here
get_ipython().run_line_magic('run', 'data_representation.ipynb')
get_ipython().run_line_magic('run', 'predictors.ipynb')


# In[ ]:


def calculate_accuracy(predictions, actual):
    if len(predictions) == 0:
        return 0.0

    correct = 0
    for i in range(len(predictions)):
        if predictions[i] == actual[i]:
            correct += 1

    return correct / len(predictions)


# In[ ]:


def main():

    # Load datasets
    historical = DataTable("data/cancer_historical.csv")
    new_cases = DataTable("data/cancer_new_cases.csv")
    labels = DataTable("data/cancer_new_cases_labels.csv")


    # Create predictors
    mode_predictor = MajorityClassPredictor(historical)
    nn_predictor = NearestNeighborPredictor(historical)


    mode_predictions = []
    nn_predictions = []
    actual_labels = []   # true labels of the cases that were predicted


    # Predict every new case
    for i in range(len(new_cases.data)):

        patient = new_cases.get_row(i)

        try:
            mode_prediction = mode_predictor.predict(patient)
            nn_prediction = nn_predictor.predict(patient)

            # these lines only run if neither predict raised an error
            mode_predictions.append(mode_prediction)
            nn_predictions.append(nn_prediction)

            # Get true label
            actual_labels.append(labels.get(i, "TumorType"))

        except OutOfSampleError as e:
            # no prediction is made for this case, so it is left out
            print(f"Case {i} skipped. OutOfSampleError: {e}")


    # Accuracy
    print("Cases predicted:", len(actual_labels), "of", len(new_cases.data))

    print(
        "Mode accuracy:",
        calculate_accuracy(mode_predictions, actual_labels)
    )

    print(
        "Nearest Neighbor accuracy:",
        calculate_accuracy(nn_predictions, actual_labels)
    )


# In[ ]:


main()

