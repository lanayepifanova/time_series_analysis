def calculate_moving_average(df, window=7):
    """Calculates the moving average and adds it to the DataFrame."""
    if df is None:
        return None
    df['Moving Average'] = df['Value'].rolling(window=window).mean()
    return df
