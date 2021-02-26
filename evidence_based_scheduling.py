import sys
import pandas as pd
import numpy as np
import datetime as dt
from pandas.tseries.offsets import BDay
from datetime import date

def estimate(effort, file_path):
    past_work = calculate_actual(completed_tickets(file_path))

    velocities = calculate_velocities(past_work)['velocity']
    simulations = simulate_from(velocities)

    days_required = simulations.ge(effort).idxmax(axis="columns").quantile(0.95)
    return (date.today() + BDay(1)).date().strftime("%B %d, %Y")


def simulate_from(velocities):
    random_samples = velocities.sample(n=1500000, replace=True)
    simulations = random_samples.values.reshape((10000, 150))
    return pd.DataFrame(simulations.cumsum(axis=1))

def calculate_velocities(completed_tickets_with_actual):
    completed_tickets_with_actual['velocity'] = completed_tickets_with_actual['estimate'] / completed_tickets_with_actual['actual']
    return completed_tickets_with_actual

def calculate_actual(completed_tickets):
    completed_tickets['actual'] = np.vectorize(business_days_between)(completed_tickets['start_date'], completed_tickets['end_date'])
    return completed_tickets

def completed_tickets(file_path):
    return load_estimates(file_path).dropna()

def load_estimates(file_path):
    estimates = pd.read_csv(file_path, sep='\t')
    estimates = format_dates_for(estimates, 'start_date')
    return format_dates_for(estimates, 'end_date')

def format_dates_for(df, column):
    df[column] = pd.to_datetime(df[column], format='%Y-%m-%d')
    df[column] = df[column].dt.date
    return df

def business_days_between(start, end):
    return np.busday_count(start, end) + 1

if __name__ == "__main__":
    effort = int(sys.argv[1])
    records = sys.argv[2]
    print(estimate(effort, records))
