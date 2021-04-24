"""
PLOT AND EXCEL FOR THE REPORT
"""
import matplotlib.pyplot as plt
import numpy as np
import os

def plot(df):
    # Plot and save the figure.
    plt.style.use('ggplot')

    
    # Rearrange the dataframe.
    df = df.T

    _, ax = plt.subplots()
    df.plot(linestyle='--', marker='o', ax=ax)

    # Set labels and a title.
    plt.xlabel('Input size n', fontstyle='italic')
    plt.ylabel('Running time (milliseconds)', fontstyle='italic')
    plt.title('Sorting Benchmark', y=1.05, fontsize=13)

    # Move legend outside the plot.
    leg = plt.legend(bbox_to_anchor=(1, 1), loc='best')

    # Save the plot.
    plt.savefig('assets/benchmark_plot.png', bbox_inches='tight')
    return leg, ax


def big_o_chart_and_excel(df):
    # Create a new directory 'assets'
    # if it doesn't exist.
    if not os.path.isdir('assets'):
        os.mkdir('assets')

    # Save the dataframe as an excel file.
    df.to_excel('assets/benchmark_results.xlsx')

    # Plot the benchmarks.
    leg, ax = plot(df)

    # Fill the space with colour for Big O.
    # Adapted from https://www.statology.org/matplotlib-fill-between/
    x = np.arange(100100)
    y = x * 2
    excellent = ax.fill_between(x, np.ones(x.shape)+300, facecolor='darkgreen', label='excellent',interpolate=True)
    good = ax.fill_between(x, x*0.2, facecolor='limegreen', label='good', interpolate=True,  alpha=0.5)
    fair = ax.fill_between(x, y, facecolor='yellow',label='fair', interpolate=True,  alpha=0.5)
    bad = ax.fill_between(x, y, x/2, facecolor='orange',label='bad', interpolate=True,  alpha=0.5)
    horrible = ax.fill_between(x, y, np.max(y)+35000, facecolor='red', label='horrible', interpolate=True,  alpha=0.5)
    
    # Limit the axis.
    plt.xlim(0, 10100)
    plt.ylim(0, 55000)

    # Split the legend into two.
    # https://matplotlib.org/2.0.2/users/legend_guide.html
    
    ax.add_artist(leg)
    plt.legend(handles=[excellent, good, fair, bad, horrible], ncol=5, bbox_to_anchor=(1.04, 1), loc=4, frameon=False)
    plt.title('Big O Notation', y=1.09, fontsize=13)

    # Save the plot and close.
    plt.savefig('assets/big_o_notation_plot.png', bbox_inches="tight")
    plt.close()
