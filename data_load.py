import pandas as pd

def load_data(filepath='time_series_data.csv'):
    """Loads time series data from a CSV file."""
    try:
        df = pd.read_csv(filepath, parse_dates=['Date'], index_col='Date')
        return df
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except Exception as e:
        print(f"An error occured:{e}")
        return None
