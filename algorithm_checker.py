"""
Checking each algorithm for correctness by comparing the result
with in-built sorted function
"""

from random import shuffle
from sorting_algorithms import insertion_sort, quicksort, heap_sort, bucket_sort, introsort

# Create a shuffled array of size 5000
arr = list(range(5000))
shuffle(arr)

# Compare each algorithm to sorted function
if insertion_sort(arr) == sorted(arr):
    print(f'Insertion sort -> {True}')

if quicksort(arr) == sorted(arr):
    print(f'Quicksort -> {True}')

if heap_sort(arr) == sorted(arr):
    print(f'Heap sort -> {True}')

if bucket_sort(arr) == sorted(arr):
    print(f'Bucket sort -> {True}')

if introsort(arr)  == sorted(arr):
    print(f'Introsort -> {True}')
