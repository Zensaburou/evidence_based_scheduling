import pdb
from evidence_based_scheduling import *
from prediction import *

def test_load_estimate():
    predict('./data/test.tsv', './data/test_predictions.tsv')
