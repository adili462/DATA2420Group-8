from data_representation import DataTable
from predictors import MajorityClassPredictor, NearestNeighborPredictor
from exceptions import OutOfSampleError


def calculate_accuracy(predictions: list, actual: list) -> float:
    """
    Calculate prediction accuracy.
    :param predictions: list of predicted tumor types
    :param actual: list of the true tumor types (same order)
    :return: fraction of predictions that were correct (0 to 1)
    """
    if len(predictions) != len(actual):
        raise ValueError("predictions and actual must be the same length")
    if len(predictions) == 0:
        raise ValueError("there are no predictions to check")

    correct = 0
    for i in range(len(predictions)):
        if predictions[i] == actual[i]:
            correct += 1

    return correct / len(predictions)


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
    actual_labels = []

    # Predict every new case
    for i in range(len(new_cases.data)):

        patient = new_cases.get_row(i)

        try:
            mode_prediction = mode_predictor.predict(patient)
            nn_prediction = nn_predictor.predict(patient)

            mode_predictions.append(mode_prediction)
            nn_predictions.append(nn_prediction)

            # only keep the true label if this patient got a prediction,
            # so the lists stay lined up
            actual_labels.append(int(labels.get(i, "TumorType")))

        except OutOfSampleError as e:
            print("Patient", i, "skipped. OutOfSampleError:", e)

    print("Number of predictions:", len(actual_labels))

    # Accuracy
    mode_accuracy = calculate_accuracy(mode_predictions, actual_labels)
    nn_accuracy = calculate_accuracy(nn_predictions, actual_labels)

    print("Mode accuracy:", mode_accuracy)
    print("Nearest Neighbor accuracy:", nn_accuracy)


if __name__ == "__main__":
    main()
