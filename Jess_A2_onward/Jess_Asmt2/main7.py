from data_representation import DataTable
from predictors import MajorityClassPredictor, NearestNeighborPredictor
from exceptions import OutOfSampleError
from pathlib import Path

def calculate_accuracy(predictions, actual):
    """
    Calculate prediction accuracy.
    """
    #for prd in predictions:



def main():

    # Load datasets
    historical = DataTable(str(Path(__file__).parent / 'Data/cancer_historical1.csv'))
    new_cases = DataTable(str(Path(__file__).parent / "Data/cancer_new_cases1.csv"))
    labels = DataTable(str(Path(__file__).parent / "Data/cancer_new_cases_labels1.csv"))

    '''uncomment this once ready for predictions'''

    # Create predictors by feeding historical DataTable in
    mode_predictor = MajorityClassPredictor(historical)
    nn_predictor = NearestNeighborPredictor(historical)


    mode_predictions = []
    nn_predictions = []
    
    # find hist range of each feature before iterating thru all patients
    col_names = [
        col_name
        for col_name in historical.get_column_names()
        if col_name != "TumorType"
    ]
    # create list of column names (features) before iterating thru all patients
    for feat in col_names:
        min_hist, max_hist = nn_predictor.feature_ranges[feat]
        print(f"Historical range for {feat}: {min_hist, max_hist}")

    # Predict every new case
    for i in range(len(new_cases)):

        patient = new_cases.get_row(i)

        try:
            mode_predictions.append(
                mode_predictor.predict(patient)
            )

            nn_predictions.append(
                nn_predictor.predict(patient, col_names, min_hist, max_hist)
            )
            
        except OutOfSampleError as e:
            print(e)
            "add exceptional patient value (outside of 1-10)!!!"
    print(nn_predictions)
    # Get true labels
    actual_labels = labels.get_column("TumorType")


    # Accuracy
    print(
        "Mode accuracy:",
        calculate_accuracy(mode_predictions, actual_labels)
    )

    print(
        "Nearest Neighbor accuracy:",
        calculate_accuracy(nn_predictions, actual_labels)
    )


if __name__ == "__main__":
    main()