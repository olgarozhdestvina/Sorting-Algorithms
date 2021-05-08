""" CTA Project on Sorting Algorithms
Computational Thinking with Algorithms Module GMIT 2021
Lecturer: Dominic Carr
Completed by Olga Rozhdestvina

Application to benchmark five different sorting algorithms.
"""

from time import time
import numpy as np
import pandas as pd
from sortingAlgorithms import insertion_sort, quicksort, heap_sort, bucket_sort, introsort
from assetsForReport import excel_and_plots_for_report, save_benchmark_plots


"""
TIME BENCHMARK
"""


def shuffled_array(array):
    """ Shuffle an array using a numpy random number generator """

    rng = np.random.default_rng()
    rng.shuffle(array)
    return array


def average_running_time(input_sizes, sorting_algorithm):
    """ Find average running time (in milliseconds) 
    for a sorting algorithm for each input size array """

    running_time_average = []

    # For each input size generate a new array.
    for i in input_sizes:
        time_diff_sum = 0
        arr = list(range(i))

        for _ in range(10):
            # Shuffle the array and measure the time it took to sort it.
            shuffled = shuffled_array(arr)

            start_time = time()
            sorting_algorithm(shuffled)
            time_diff = time() - start_time

            # Sum up the runtimes.
            time_diff_sum += time_diff

        # Find the average, convert to ms,
        # round to 3 decimal places and append to the list.
        running_time_average_sec = (time_diff_sum / 10) * 1000
        running_time_average.append(round(running_time_average_sec, 3))

    return running_time_average


def benchmark_runner(sorting_algorithms, input_sizes):
    """ Creating a list of benchmark results """

    benchmarks = []

    # Run benchmark for each sorting algorithm.
    for sorting_algorithm in sorting_algorithms:
        running_time_average = average_running_time(
            input_sizes, sorting_algorithm)
        benchmarks.append(running_time_average)

    return benchmarks


def results_as_dataframe(input_sizes, benchmarks, algorithm_names):
    """ Dateframe format of benchmarking results """

    # Creating a dataframe with input sizes for columns
    # and algorithm names for the index.
    df = pd.DataFrame(index=algorithm_names, columns=input_sizes)
    df.columns.name = 'Sizes'

    # Add the results into the dataframe.
    for i in range(len(algorithm_names)):
        df.iloc[i] = benchmarks[i]

    return df


# Driver code.
if __name__ == '__main__':

    # Input sizes for sorting.
    input_sizes = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 
                    6250, 7500, 8750, 10000, 100000, 200000, 300000, 500000]

    # A list of algorithms.
    sorting_algorithms = [insertion_sort, quicksort,
                          heap_sort, bucket_sort, introsort]
    algorithm_names = ['Insertion Sort', 'Quicksort',
                       'Heap Sort', 'Bucket Sort', 'Introsort']

    # Run benchmarks for all sorting algorithms for input size up to 10000
    benchmarks = benchmark_runner(sorting_algorithms, input_sizes[:-4])
    benchmark_results = results_as_dataframe(
        input_sizes[:-4], benchmarks, algorithm_names)

    # Save excel, plot and big O charts.
    excel_and_plots_for_report(benchmark_results, 'assets/benchmark_results.xlsx',
                               'assets/benchmark_plot.png', (0, 10200), (-500, 60000), 'assets/big_o_notation_plot.png')
    save_benchmark_plots(benchmark_results[1:], 'assets/benchmark_plot_excl_insertion_sort.png',
                         (0, 10200), (-10, 1000), 'assets/big_o_notation_plot_excl_insertion_sort.png')

    # Separate benchmark for Quicksort and Introsort for input sizes 30000 - 150000
    benchmarks_quicksort_vs_introsort = benchmark_runner(
        sorting_algorithms[1:5:3], input_sizes[-4:])
    benchmark_results_quicksort_vs_introsort = results_as_dataframe(
        input_sizes[-4:], benchmarks_quicksort_vs_introsort, algorithm_names[1:5:3])

    # Save excel and big O charts.
    save_benchmark_plots(benchmark_results_quicksort_vs_introsort,
                         'assets/benchmark_plot_quicksort_vs_introsort.png',
                         (99500, 500500), (-50, 7000), 'assets/big_o_notation_plot_quicksort_vs_introsort.png')

    # Output benchmark results into the console.
    headers = [benchmark_results.columns.name] + \
        list(benchmark_results.columns)
    print(benchmark_results.to_markdown(tablefmt="grid", headers=headers))
