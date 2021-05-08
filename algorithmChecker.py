"""
Checking each algorithm for correctness by comparing the result
with in-built sorted function
"""

import numpy as np
from sortingAlgorithms import insertion_sort, quicksort, heap_sort, bucket_sort, introsort


def shuffled_array(array):
    """ Shuffle an array using a numpy random number generator """

    rng = np.random.default_rng()
    rng.shuffle(array)
    return array


arr = shuffled_array(list(range(5000)))

if insertion_sort(arr) == sorted(arr):
    print('Insertion sort ->', True)
if quicksort(arr) == sorted(arr):
    print('Quicksort ->', True)
if heap_sort(arr) == sorted(arr):
    print('Heap sort ->', True)
if bucket_sort(arr) == sorted(arr):
    print('Bucket sort ->', True)
if introsort(arr) == sorted(arr):
    print('Introsort ->', True)