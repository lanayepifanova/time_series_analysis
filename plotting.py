import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

def plot_time_series(df, title='Time Series Data'):
    """Plots the time series data."""
    if df is None:
        return
    plt.figure(figsize=(12, 6))
    plt.plot(df['Value'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

def plot_moving_average(df, window=7):
    """Calculates and plots the moving average."""
    if df is None:
        return
    df['Moving Average'] = df['Value'].rolling(window=window).mean()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Value'], label='Original Data')
    plt.plot(df['Moving Average'], label=f'{window}-day Moving Average')
    plt.title('Time Series with Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_autocorrelation(df, lags=40):
    """Plots the autocorrelation function."""
    if df is None:
        return
    plt.figure(figsize=(12, 6))
    plot_acf(df['Value'], lags=lags, ax=plt.gca())
    plt.title('Autocorrelation Function')
    plt.xlabel('Lags')
    plt.ylabel('Autocorrelation')
    plt.grid(True)
    plt.show()
