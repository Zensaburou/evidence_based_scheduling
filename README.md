## Requirements

* Python 3.9.1
* [Pipenv](https://pypi.org/project/pipenv/)

## Setup

* `$ pipenv install`
* `$ pipenv shell`

## Usage

* `$ python evidence_based_scheduling.py 10 ./data/my_data.tsv`

Where `10` is the estimated effort, and `./data/my_data.tsv` is a record of past work.
See `./data/test.tsv` for an example record format.

### Prediction File

Alternatively, users can generate predictions using a specially formatted tsv:

* `$ python prediction.py ./data/my_data.tsv ./data/predictions.tsv`

Where `./data/my_data.tsv` is the same as above, and `./data/predictions.tsv` is the formatted tsv.
For an example format, see `./data/test_predictions.tsv`.

Estimates will be generated for any row with a `null` prediction column.
