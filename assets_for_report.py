"""
PLOT AND EXCEL FOR THE REPORT
"""

import matplotlib.pyplot as plt
import numpy as np
import os


def excel_file(df, filename):
    """ Creating a new folder and saving excel file to it. """

    # Create a new directory 'assets'
    # if it doesn't exist.
    if not os.path.isdir('assets'):
        os.mkdir('assets')

    # Save the dataframe as an excel file.
    df.to_excel(filename)


def benchmark_plot(df, plot_name):
    """ Plot performace of soting algorithms and save it. """

    # Plot the data.
    plt.style.use('bmh')
    _, ax = plt.subplots(figsize=(12, 9))
    df = df.T
    df.plot(linestyle='--', marker='o', ax=ax)

    # Set labels and a title.
    plt.xlabel('Input size n', fontstyle='italic')
    plt.ylabel('Running time (milliseconds)', fontstyle='italic')
    plt.title('Running time Benchmark', y=1.05, fontsize=13)

    # Move legend outside the plot.
    plt.legend(bbox_to_anchor=(1, 1), loc='best')
    plt.savefig(plot_name, bbox_inches='tight')


def big_o_plot(df, n, big_o_notation, big_o_labels, big_o_plot_name):
    """ Plot comparing the expected Big O time complexity vs benchmark results. """

    # Labels and titles for the plot.
    benchmarks = ['Insertion Sort', 'Quicksort',
                  'Heap Sort', 'Bucket Sort', 'Introsort']

    # Plot the data over 5 subplots.
    fig, axs = plt.subplots(5, 1, figsize=(
        15, 10), tight_layout=True, sharex=True)
    # Common ylabel for matplotlib subplots. Adapted from
    # https://stackoverflow.com/questions/16150819/common-xlabel-ylabel-for-matplotlib-subplots
    fig.text(0, 0.4, 'Running time (milliseconds)', ha='center',
             rotation='vertical', fontsize=12, fontstyle='italic')

    # Plot benchmark and big o per each set of axis.
    for axs, big_o, big_o_label, benchmark_name in zip(axs, big_o_notation, big_o_labels, benchmarks):
        axs.plot(n, big_o, label=big_o_label)
        axs.plot(df[benchmark_name], label=benchmark_name,
                 linestyle='--', marker='o')
        axs.set_title(benchmark_name)
        axs.legend(loc=2)

    # Save the figure.
    plt.xlabel('Input size n', fontstyle='italic')
    plt.savefig(big_o_plot_name, bbox_inches="tight")
    plt.close()


def excel_and_plots_for_report(df, filename, plot_name):
    """ Excel and plots with all benchmarks. 
    Big plot compares benchmarks with originally anticipated time compexity
    and then with a better fitting time complexity.
    """
    excel_file(df, filename)
    benchmark_plot(df, plot_name)

    df = df.T
    
    # Plot with expected Big O time complexity.
    n = np.linspace(100, 15000)
    expected_big_o = [n**2, n * np.log(n), 
                        n * np.log(n), np.log(n), n * np.log(n)]
    expected_big_o_labels = ['Quadratic', 'Log Linear',
                             'Log Linear', 'Logarithmic', 'Log Linear']
    big_o_plot(df, n, expected_big_o, expected_big_o_labels,
               'assets/expected_big_o_plot.png')

    # Plot with closer fitting Big O time complexity.
    closer_fitting_big_o = [n * np.log(n), n,  n, np.log(n), n]
    closer_fitting_big_o_labels = ['Log Linear', 'Linear',
                                   'Linear', 'Logarithmic', 'Linear']
    big_o_plot(df, n, closer_fitting_big_o, closer_fitting_big_o_labels,
               'assets/closer_fitting_big_o_plot.png')
