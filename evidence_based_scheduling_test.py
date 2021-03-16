import pdb
from evidence_based_scheduling import *

def test_load_estimate():
    data = completed_tickets('./data/test.tsv')
    data = calculate_actual(data)
    data = calculate_velocities(data)
    simulation = simulate_from(data['velocity'])
