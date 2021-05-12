""" SORTING ALGORITHMS: 
        * Insertion sort
        * Quicksort
        * Heap sort
        * Bucket sort
        * Introsort
"""

import numpy as np

# 1. Insertion sort
# https://brilliant.org/wiki/insertion/


def insertion_sort(array, begin=1, end=None):
    """ Sorting is done by splitting the array into a sorted and 
    an unsorted part. Values from the unsorted part are selected 
    and moved to their correct position in the sorted part. """

    # None is initiated to be used in Introsort implementation
    if end == None:
        end = len(array)

    # Loop through the array
    for slot in range(begin, end):

        # Select the element to position in its correct place
        current_value = array[slot]

        # Initialize a variable for finding the correct position of
        # the current value
        position = slot

        # Loop through the array and find the correct position
        # of the element referenced by current_value
        while position > 0 and array[position-1] > current_value:

            # Shift the value to the left and reposition position
            # to point to the next element (from right to left)
            array[position] = array[position-1]
            position -= 1

        # When shifting is finished,
        # position the current_value in its correct location
        array[position] = current_value

    return array


# 2. Quicksort.
# https://brilliant.org/wiki/quick-sort/

def quicksort(array):
    """ Sorting is done by selecting an element as pivot 
    to partition the array around the picked pivot. """

    # Base case for the recursion where there is
    # only one element in the array.
    length = len(array)
    if length < 2:
        return array

    # Randomly select a pivot
    pivot = array[np.random.randint(0, length - 1)]

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


# 3. Heap sort
# https://brilliant.org/wiki/heap-sort/

def heap_sort(array):
    """ Sort an array of a given size """

    def build_heap(array, heap_size):
        """ Building max heap """
        for i in range((heap_size//2), -1, -1):

            # Check for max-heap property
            max_heapify(array, heap_size, i)

    def max_heapify(array, heap_size, i):
        """ Function for maintaining the max-heap property: meaning 
        that a node can't have a greater value than its parent."""

        # Initialize the largest as a root
        largest = i

        # And then left and right children
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left or right child exists and if either
        # is greater than a root. If yes, make it the largest.
        if left < heap_size and array[left] > array[largest]:
            largest = left
        if right < heap_size and array[right] > array[largest]:
            largest = right

        # If changes are needed, swap the root with the largest
        if largest != i:
            array[i], array[largest] = array[largest], array[i]

            # Heapify the root now with the largest
            max_heapify(array, heap_size, largest)

    heap_size = len(array)

    # Build the heap
    build_heap(array, heap_size)

    # Extracting elements one by one
    for i in range(heap_size-1, 0, -1):

        # Swap the first element with the current
        array[0], array[i] = array[i], array[0]
        heap_size -= 1

        # Check for max-heap property
        max_heapify(array, heap_size, 0)
    
    return array


# 4. Bucket Sort
# https://stackabuse.com/bucket-sort-in-python/

def bucket_sort(array):
    """ The function for bucket sort implementation assigning 
    array elements into corresponding buckets and then recombining
    the buckets into a sorted array.

    The implementation is simplified since the input is always
    equally distributed in a range [0, max].
    """

    # Create a number of empty buckets to match the array length
    length = len(array)
    bucket_list = [[] for _ in range(length)]

    # Distribute elements among buckets where bucket index
    # is equal to the current element index 
    for i in range(length):
        bucket_list[array[i]].append(array[i])

    # Concatenate the buckets
    output = []
    for bucket in range(length):
        output += bucket_list[bucket]
        
    return output


# 5. Introsort
# https://gist.github.com/Alfex4936/e8b6b7c06a181d3faa84b155b20e6de6

def introsort(array):
    """ The function to run introsort_helper with initial parameters """

    length = len(array)

    # Set the maximum depth for recursion and a threshold
    max_depth = 2 * (length.bit_length() - 1)
    size_threshold = 16

    return introsort_helper(array, 0, length, size_threshold, max_depth)


def introsort_helper(array, start, end, size_threshold, depth_limit):
    """ The main function of Introsort implementation where
    low is a starting index, high - ending index, 
    size_threshold - to compare the size of the array,
    depth_limit - maximum depth for recursion.
    """

    def median_of_3(array, low_idx, mid_idx, high_idx):
        """ The function to find the median of the three elements
        in the index low_idx, mid_idx, high_idx """

        if (array[low_idx] - array[mid_idx]) * (array[high_idx] - array[low_idx]) >= 0:
            return array[low_idx]

        elif (array[mid_idx] - array[low_idx]) * (array[high_idx] - array[mid_idx]) >= 0:
            return array[mid_idx]
        else:
            return array[high_idx]

    def get_partition(array, low, high, pivot):
        """ Partial implementation of a quicksort to get the correct place
        for pivot and get its index. It then will be used as a partition 
        to split the array into smaller parts for futher sorting.
        """

        # Compare each element of the array to the pivot.
        while True:
            while array[low] < pivot:
                # Increase the number of elements
                # that are smaller than pivot
                low += 1

            # Decrease the number of elements
            # that are bigger than pivot
            high -= 1

            while pivot < array[high]:
                high -= 1

            if low >= high:
                return low

            # If high > low then swap the elements with low and high indexes
            array[low], array[high] = array[high], array[low]
            low += 1

    # If the array is large, call either heap sort or quicksort
    while end - start > size_threshold:
        # if the recursion limit is occurred call heap sort
        if depth_limit == 0:
            return heap_sort(array)

        # Decrease the level of recursion
        depth_limit -= 1

        # Find the pivot to get partition
        pivot = median_of_3(array, start, start +
                            ((end - start) // 2) + 1, end - 1)

        # array[partitionPoint] is now at right place
        partition = get_partition(array, start, end, pivot)

        # Sort elements before and after the partitioning index
        introsort_helper(array, partition, end, size_threshold, depth_limit)
        end = partition

    # Call the Insertion sort if the size of the array is small
    return insertion_sort(array, start, end)
