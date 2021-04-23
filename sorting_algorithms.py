import numpy as np

# 1. Insertion sort
# https://brilliant.org/wiki/insertion/

def insertion_sort(array):

    # Loop through the array starting from its second element
    for slot in range(1, len(array)):

        # Select the element to position in its correct place
        current_value = array[slot]

        # Initialize a variable for finding the correct position of the current value
        position = slot - 1

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
# https://brilliant.org/wiki/quick-sort/

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


# 3. Heap sort
# https://brilliant.org/wiki/heap-sort/

def max_heapify(array, heap_size, i):

    """ Function for maintaining the max-heap property:
    meaning that a node can't have a greater value than its parent."""

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


def build_heap(array, heap_size):
    """ Building max heap """
    for i in range((heap_size//2), -1, -1):

        # Check for max-heap property
        max_heapify(array, heap_size, i)


def heap_sort(array):
    """ Sort an array of a given size """

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


# 4. Counting Sort

# 5. IntroSort