""" CTA Project on Sorting Algorithms
Computational Thinking with Algorithms Module GMIT 2021
Lecturer: Dominic Carr
Completed by Olga Rozhdestvina

Application to benchmark five different sorting algorithms.
"""

from time import time
from random import shuffle
from pandas import DataFrame
from sorting_algorithms import insertion_sort, quicksort, heap_sort, bucket_sort, introsort
from assets_for_report import excel_and_plots_for_report, benchmark_plot

"""
TIME BENCHMARK
"""


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
            shuffle(arr)

            start_time = time()
            sorting_algorithm(arr)
            time_diff = time() - start_time

            # Sum up the runtimes.
            time_diff_sum += time_diff

        # Find the average, convert to ms,
        # round to 3 decimal places and append to the list.
        running_time_average_ms = (time_diff_sum / 10) * 1000
        running_time_average.append(round(running_time_average_ms, 3))

    return running_time_average


def benchmark_runner(input_sizes):
    """ Creating a list of benchmark results """

    # # Run benchmark for each sorting algorithm and add results into a list.
    sorting_algorithms = [insertion_sort, quicksort,
                          heap_sort, bucket_sort, introsort]
    benchmarks = [average_running_time(
        input_sizes, sorting_algorithm) for sorting_algorithm in sorting_algorithms]

    return benchmarks


def results_as_dataframe(input_sizes, benchmarks):
    """ Dateframe format of benchmarking results """

    algorithm_names = ['Insertion Sort', 'Quicksort',
                       'Heap Sort', 'Bucket Sort', 'Introsort']

    # Creating a dataframe with input sizes for columns
    # and algorithm names for the index.
    df = DataFrame(index=algorithm_names, columns=input_sizes)
    df.columns.name = 'Sizes'

    # Add the results into the dataframe.
    for i in range(len(algorithm_names)):
        df.iloc[i] = benchmarks[i]

    return df


# Driver code.
if __name__ == '__main__':

    # Input sizes for sorting.
    input_sizes = [100, 250, 500, 750, 1000, 1250, 2500, 5000,
                  6250, 7500, 8750, 10000, 15000]

    # Run benchmarks and transfer it to a data frame
    benchmarks = benchmark_runner(input_sizes)
    benchmark_results = results_as_dataframe(input_sizes, benchmarks)

    # Output benchmark results into the console.
    headers = [benchmark_results.columns.name] + \
        list(benchmark_results.columns)
    print(benchmark_results.to_markdown(tablefmt="grid", headers=headers))

    # Save excel, plot and big O charts
    # 2 plots (for all sorts and excluding insetion sort)
    # 2 big o plots for originally expected time complexity and adjusted estimation.
    benchmark_plot(benchmark_results[1:],
                   'assets/benchmark_plot_excl_insertion_sort.png')
    excel_and_plots_for_report(benchmark_results, 'assets/benchmark_results.xlsx',
                               'assets/benchmark_plot.png')
