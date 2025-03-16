from data_loader import load_data
from plotting import plot_time_series, plot_moving_average, plot_autocorrelation
from analysis import calculate_moving_average

def main():
    """Main function to execute the analysis."""
    df = load_data()
    if df is not None:
        plot_time_series(df)
        calculate_moving_average(df)
        plot_moving_average(df)
        plot_autocorrelation(df)

if __name__ == "__main__":
    main()
