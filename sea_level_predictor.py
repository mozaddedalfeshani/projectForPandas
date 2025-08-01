import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', alpha=0.6)

    # 3. Line of best fit (full data)
    res_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_full = pd.Series(range(1880, 2051))
    y_full = res_full.intercept + res_full.slope * x_full
    ax.plot(x_full, y_full, 'r', label='Fit: 1880-2050')

    # 4. Line of best fit (year >= 2000)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    ax.plot(x_recent, y_recent, 'g', label='Fit: 2000-2050')

    # 5. Labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()

    # 6. Save and return plot
    plt.tight_layout()
    fig.savefig('sea_level_plot.png')
    return fig
