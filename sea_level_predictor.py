import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter(x, y, s=1)
    
    # Create first line of best fit
    lin_regress_1 = linregress(x, y)
    intercept_1 = lin_regress_1.intercept
    slope_1 = lin_regress_1.slope

    x_1 = pd.concat([x, pd.Series([2050])], ignore_index=True)
    y_1 = intercept_1 + slope_1 * x_1

    plt.plot(x_1, y_1, 'y')

    # Create second line of best fit
    x = df.loc[df['Year'] >= 2000, ['Year']].squeeze()
    y = df.loc[df['Year'] >= 2000, ['CSIRO Adjusted Sea Level']].squeeze()
    
    lin_regress_2 = linregress(x, y)
    intercept_2 = lin_regress_2.intercept
    slope_2 = lin_regress_2.slope

    y_2 = intercept_2 + slope_2 * x

    plt.plot(x, y_2, 'r')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()