import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 8))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.7, s=20)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line_x = range(1880, 2051)
    line_y = slope * line_x + intercept
    plt.plot(line_x, line_y, 'r', label=f'Line of best fit (1880-2013)', linewidth=2)

    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    line_x_recent = range(2000, 2051)
    line_y_recent = slope_recent * line_x_recent + intercept_recent
    plt.plot(line_x_recent, line_y_recent, 'g', label=f'Line of best fit (2000-2013)', linewidth=2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()