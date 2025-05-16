## How It Works
- Reads a CSV file (`data.csv`) with two columns: `Date` and `Value`
- Automatically determines whether the data is daily, monthly, or yearly
- Forecasts future values using the Holt-Winters method (Exponential Smoothing)
- Plots both historical and predicted values

## Dependencies

```bash
pip install pandas matplotlib statsmodels

## How to Run

Clone this repository or download the folder

Make sure you have Python 3 installed

Place your data in data.csv format:

'''csv
Date,Value
2023-01-01,120
2023-02-01,130
...

## Run the script 

python pmodel.py

## Output
A window will open with the forecast plot

Predicted values extend 30 steps into the future