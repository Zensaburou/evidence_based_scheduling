from evidence_based_scheduling import *
from datetime import date
import numpy as np

def predict(estimates_file, prediction_file):
    predictions = pd.read_csv(prediction_file, sep='\t')

    needing_predictions = predictions[predictions['prediction'].isnull()]
    needing_predictions['created_at'] = date.today().strftime("%Y-%m-%d")
    needing_predictions['prediction'] = np.vectorize(estimate)(needing_predictions['points_remaining'], estimates_file)

    predictions = predictions.dropna()

    return pd.concat([predictions, needing_predictions])

if __name__ == "__main__":
    estimates_file = sys.argv[1]
    prediction_file = sys.argv[2]

    predictions = predict(estimates_file, prediction_file)
    print(predictions.to_csv(sep="\t", index=None))
