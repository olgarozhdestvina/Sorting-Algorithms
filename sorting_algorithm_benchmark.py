""" CTA Project on Sorting Algorithms
Computational Thinking with Algorithms Module GMIT 2021
Lecturer: Dominic Carr
Completed by Olga Rozhdestvina


Application to benchmark five different sorting algorithms.
Implementations are taken from:
Santiago Valdarrama, Real Python, Sorting Algorithms in Python,[ONLINE] Available at: https://realpython.com/sorting-algorithms-python/. [Accessed 20 April 2021].

"""

from time import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


""" ALGORITHMS """

# 1. Insertion sort

def insertion_sort(array):

    # Loop through the array starting from its second element
    for i in range(1, len(array)):

        # Select the element to position in its correct place
        current_value = array[i]

        # Initialize a variable for finding the correct position of the current value
        position = i - 1

        # Loop through the array and find the correct position
        # of the element referenced by current_value
        while position >= 0 and array[position] > current_value:

            # Shift the value to the left and reposition position
            # to point to the next element (from right to left)
            array[position + 1] = array[position]
            position -= 1

        # When shifting is finished,
        # position the current_value in its correct location
        array[position + 1] = current_value

    return array


# 2. Quicksort.

def quicksort(array):
    # Base case for the recursion where there is 
    # only one element in the array.
    if len(array) < 2:
        return array

    # Randomly select a pivot
    pivot = array[np.random.randint(0, len(array) - 1)]

    # Loop through the array and compare each element to the pivot. 
    # If they are smaller --> add to the low list.
    # If bigger --> to the high list.
    # If same --> the same list.
    low, same, high = [], [], []

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)

    # Combine the lists into one in the low-same-high order.
    return quicksort(low) + same + quicksort(high)


"""
RUNNING TIME BENCHMARK
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
        arr = np.arange(i)

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


def benchmark_runner(input_sizes):
    """ Creating a list of benchmark results """
    
    # A list of algorithms.
    sorting_algorithms = [insertion_sort, quicksort] # ,heap_sort, radix_sort, counting_sort, introsort]
    benchmarks = []

    # Run benchmark for each sorting algorithm.
    for sorting_algorithm in sorting_algorithms:
        running_time_average = average_running_time(input_sizes, sorting_algorithm)
        benchmarks.append(running_time_average)

    return benchmarks


def results_as_dataframe(input_sizes, benchmarks):
    """ Dateframe format of benchmarking results """

    # Creating a dataframe with input sizes for columns
    # and algorithm names for the index.
    algorithm_names = ['Insertion Sort', 'Quicksort']# , 'Heap Sort', 'Radix Sort', 'Counting Sort', 'IntroSort']
    df = pd.DataFrame(index=algorithm_names, columns=input_sizes)
    df.columns.name = 'Sizes'

    # Add the results into the dataframe.
    for i in range(len(algorithm_names)):
        df.iloc[i] = benchmarks[i]
    return df


"""
PLOT AND EXCEL FOR THE REPORT
"""


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
    plt.savefig('benchmark_plot.png', bbox_inches="tight")


def big_o_chart(df):
    # Save the dataframe as an excel file.
    df.to_excel('benchmark_results.xlsx')

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
    plt.savefig('big_o_notation_plot.png', bbox_inches="tight")
    plt.close()

# Driver code to test above.
if __name__ == '__main__':
    input_sizes = [100, 250, 500, 750, 1000,
                   1250]  # , 2500, 3750, 5000, 6250, 7500, 8750, 10000]

    benchmarks = benchmark_runner(input_sizes)
    benchmark_results = results_as_dataframe(input_sizes, benchmarks)
    plot(benchmark_results)
    big_o_chart(benchmark_results)

    # Output benchmark results into the console.
    headers = [benchmark_results.columns.name] + list(benchmark_results.columns)
    print(benchmark_results.to_markdown(tablefmt="grid", headers=headers))
