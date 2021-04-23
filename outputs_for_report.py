"""
PLOT AND EXCEL FOR THE REPORT
"""
import matplotlib.pyplot as plt
import numpy as np

def plot(df):
    # Save the dataframe as an excel file.
    df.to_excel('benchmark_results.xlsx')

    # Rearrange the dataframe.
    df = df.T
    
    # Plot and save the figure.
    plt.style.use('ggplot')
    df.plot(linestyle='--', marker='o')
    plt.xlabel('Input size n', fontstyle='italic')
    plt.ylabel('Running time (milliseconds)', fontstyle='italic')
    plt.title('Sorting Benchmark', y=1.05, fontsize=13)
    plt.legend(bbox_to_anchor=(1, 1), loc='best')
    plt.savefig('assets/benchmark_plot.png', bbox_inches="tight")


def big_o_chart_and_excel(df):
    # Save the dataframe as an excel file.
    df.to_excel('assets/benchmark_results.xlsx')

    # Rearrange the dataframe.
    df = df.T
    
    # Plot and save the figure.
    plt.style.use('ggplot')
    df.plot(linestyle='--', marker='o')

    # Fill the space in between 
    # Adapted from https://www.statology.org/matplotlib-fill-between/
    x = np.arange(1500)
    y = x * 2

    plt.fill_between(x, y, np.max(y), facecolor='red', interpolate=True,  alpha=0.5)
    plt.fill_between(x, y, np.ones(x.shape)+30, facecolor='orange', interpolate=True,  alpha=0.5)
    plt.fill_between(x, np.ones(x.shape)+30, facecolor='darkgreen', interpolate=True,  alpha=0.5)
    plt.fill_between(x, x-20, y, facecolor='lightgreen', interpolate=True,  alpha=0.5)


    plt.xlabel('Input size n', fontstyle='italic')
    plt.ylabel('Running time (milliseconds)', fontstyle='italic')
    plt.title('Sorting Benchmark', y=1.05, fontsize=13)
    plt.legend(bbox_to_anchor=(1.4, 1), loc='best')
    plt.savefig('assets/big_o_notation_plot.png', bbox_inches="tight")
    plt.close()
