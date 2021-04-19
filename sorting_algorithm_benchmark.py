""" CTA Project on Sorting Algorithms
Computational Thinking with Algorithms Module GMIT 2021
Lecturer: Dominic Carr
Completed by Olga Rozhdestvina


Application to benchmark five different sorting algorithms.
Implementations are taken from:
Insertion sort: https://realpython.com/sorting-algorithms-python/#implementing-insertion-sort-in-python
"""

from time import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table



def performance(func):
    """ Decorator that measures performace of a sorting algorithm """
    def wrap_func(*args, **kwargs):

        # Register the time before and after running a sorting algorithm
        # And calculate the difference.
        time1 = time()
        res = func(*args, **kwargs)
        time_diff = time() - time1
        return res, time_diff

    return wrap_func


def shuffled_array(array):
    """ Shuffle an array using a numpy random number generator """
    rng = np.random.default_rng()
    rng.shuffle(array)
    return array


# 1. Insertion sort
@performance
def insertion_sort(array):

    # Loop through the array starting from its second element
    for i in range(1, len(array)):

        # Select the element to position in its correct place
        current_value = array[i]

        # Initialize a variable for finding the correct position of the current value
        position = i - 1

        # Loop through the array and find the correct position
        # of the element referenced by `current_value`
        while position >= 0 and array[position] > current_value:

            # Shift the value to the left and reposition position
            # to point to the next element (from right to left)
            array[position + 1] = array[position]
            position -= 1

        # When shifting is finished,
        # position the current_value in its correct location
        array[position + 1] = current_value

    return array


def benchmark(input_sizes, sorting_algorithm):
    """ Find average running time (in milliseconds) 
    for a sorting algorithm for each input size array """

    time_avg = []

    # For each input size generate a new array
    for i in input_sizes:
        time_diff_sum = 0
        arr = np.arange(i)

        for _ in range(10):
            # Shuffle the array and then sort it.
            shuffled = shuffled_array(arr)
            _, time_diff = sorting_algorithm(shuffled)

            # Sum the time differences
            time_diff_sum += time_diff

        # Find the average, convert to ms,
        # round to 3 decimal places and append to the list
        time = (time_diff_sum / 10) * 1000
        time_avg.append(np.round(time, 3))

    return time_avg


def benchmark_runner(input_sizes):
    """ Creating a list of benchmarks """
    # Run benchmark for each sorting algorithm
    sorting_algorithms = [insertion_sort]# , 'quicksort', 'heap_sort', 'radix_sort', 'counting_sort', 'introsort']

    benchmarks = []
    for sorting_algorithm in sorting_algorithms:
        benchmarks.append(benchmark(input_sizes, sorting_algorithm))

    return benchmarks


def output_to_console(input_sizes, benchmarks):
    """ Console output of benchmarking results """

    # Creating a dataframe with input sizes for columns
    # and algorithm names for the index
    algorithm_names = ['Insertion Sort']# , 'Quicksort', 'Heap Sort', 'Radix Sort', 'Counting Sort', 'IntroSort']
    df = pd.DataFrame(index=algorithm_names, columns=input_sizes)

    # Add the results into the dataframe
    for i in range(len(algorithm_names)):
        df.iloc[i] = benchmarks[i]
    plot(df)
    save_as_table(df)
    
    return df


def plot(df):
    # Style for plots.
    plt.style.use('bmh')

    # Rearrange the dataframe.
    df = df.T

    # Plot and save the figure.
    df.plot(linestyle = '--', marker = 'o')
    plt.xlabel('Input size n')
    plt.ylabel('Running time (milliseconds)')
    plt.title('Sorting Benchmark')
    plt.savefig('Benchmark.jpg', bbox_inches="tight")
    

def save_as_table(df):
    _, ax = plt.subplots() # set size frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
    table(ax, df, loc='upper right', colWidths=[0.15]*len(df.columns))  # where df is your data frame
    plt.savefig('table.png', transparent=True)




# Driver code to test above
if __name__ == '__main__':
    input_sizes = [100, 250, 500, 750, 1000,
                   1250]  # , 2500, 3750, 5000, 6250, 7500, 8750, 10000]

    benchmarks = benchmark_runner(input_sizes)
    print(output_to_console(input_sizes, benchmarks))
