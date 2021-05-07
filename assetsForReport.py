"""
PLOT AND EXCEL FOR THE REPORT
"""

import matplotlib.pyplot as plt
import numpy as np
import os


def excel_file(df):
    """ Creating a new folder and saving excel file to it. """

    # Create a new directory 'assets'
    # if it doesn't exist.
    if not os.path.isdir('assets'):
        os.mkdir('assets')

    # Save the dataframe as an excel file.
    df.to_excel('assets/benchmark_results.xlsx')


def benchmark_plot(df):
    """ Plot performace of soting algorithms and save it. """

    # Rearrange the dataframe (sothat algorithms are now columns).
    df = df.T

    # Plot the data.
    plt.style.use('bmh')
    _, ax = plt.subplots(figsize=(12, 9))
    df.plot(linestyle='--', marker='o', ax=ax)

    # Set labels and a title.
    plt.xlabel('Input size n', fontstyle='italic')
    plt.ylabel('Running time (milliseconds)', fontstyle='italic')
    plt.title('Sorting Benchmark', y=1.05, fontsize=13)

    # Move legend outside the plot.
    leg = plt.legend(bbox_to_anchor=(1, 1), loc='best')

    return leg, ax


def big_o_chart(df, leg, ax):
    """ Big O notation add-on for the benchmark plot. """

    # Fill the space with colour for Big O.
    # Adapted from https://www.statology.org/matplotlib-fill-between/
    x = np.arange(100100)
    y = x * 2
    excellent = ax.fill_between(
        x, x * 0.045, facecolor='darkgreen', label='excellent', interpolate=True)
    good = ax.fill_between(x, x*0.2, facecolor='limegreen',
                           label='good', interpolate=True,  alpha=0.5)
    fair = ax.fill_between(x, y, facecolor='yellow',
                           label='fair', interpolate=True,  alpha=0.5)
    bad = ax.fill_between(x, y, x/2, facecolor='orange',
                          label='bad', interpolate=True,  alpha=0.5)
    horrible = ax.fill_between(x, y, np.max(
        y)+35000, facecolor='red', label='horrible', interpolate=True,  alpha=0.5)

    # Split the legend into two.
    # https://matplotlib.org/2.0.2/users/legend_guide.html
    ax.add_artist(leg)
    plt.legend(handles=[excellent, good, fair, bad, horrible],
               ncol=5, bbox_to_anchor=(0.8, 1), loc=4, frameon=False)

    # Extend the x axis and give the title to the plot.
    plt.xlim(0, 15200)
    plt.title('Big O Notation', y=1.09, fontsize=13)


def save_benchmark_plots(df):
    """ Plot all benchmarks. """

    leg, ax = benchmark_plot(df)
    plt.savefig('assets/benchmark_plot.png', bbox_inches='tight')

    # Extend y axis to catch insertion sort on the Big O plot.
    big_o_chart(df, leg, ax)
    plt.ylim(-500, 220000)

    # Save the figure
    plt.savefig('assets/big_o_notation_plot.png', bbox_inches="tight")
    plt.close()


def save_benchmark_plots_excluding_insertion_sort(df):
    """ Plot the benchmarks excluding Insertion sort. """

    leg, ax = benchmark_plot(df)
    plt.savefig('assets/benchmark_plot_excl_insertion_sort.png',
                bbox_inches='tight')

    # Limit y axis on big O chart to zoom in.
    big_o_chart(df, leg, ax)
    plt.ylim(-10, 7000)

    # Save the plot.
    plt.savefig('assets/big_o_notation_plot_excl_insertion_sort.png',
                bbox_inches="tight")
    plt.close()


def excel_and_plots_for_report(df):
    """ Excel and plots with all benchmarks. """

    excel_file(df)
    save_benchmark_plots(df)
