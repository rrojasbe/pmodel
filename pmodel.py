#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# predictive_path_model/pmodel.py

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values('Date', inplace=True)
    df.set_index('Date', inplace=True)
    return df

def determine_frequency(df):
    delta = df.index.to_series().diff().dropna()
    avg_days = delta.dt.days.mean()
    if avg_days <= 1.5:
        return 'D'  # Daily
    elif avg_days <= 31:
        return 'M'  # Monthly
    else:
        return 'Y'  # Yearly

def predict(df, periods=30):
    freq = determine_frequency(df)
    model = ExponentialSmoothing(df['Value'], trend='add', seasonal=None)
    fit = model.fit()
    forecast = fit.forecast(periods)

    if freq == 'D':
        future_index = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=periods, freq='D')
    elif freq == 'M':
        future_index = pd.date_range(start=df.index[-1] + pd.DateOffset(months=1), periods=periods, freq='M')
    else:
        future_index = pd.date_range(start=df.index[-1] + pd.DateOffset(years=1), periods=periods, freq='Y')

    forecast.index = future_index
    return forecast

def plot_data(df, forecast):
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Value'], label='Historical', marker='o')
    plt.plot(forecast.index, forecast.values, label='Predicted', linestyle='--', marker='x')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Predictive Path Model')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    file_path = 'data.csv'  # sample doc I put here that can be replaced
    df = load_data(file_path)
    forecast = predict(df)
    plot_data(df, forecast)

