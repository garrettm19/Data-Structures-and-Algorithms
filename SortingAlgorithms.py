import random
import timeit

# Helper function to print a list
def print_list(arr):
    print(" ".join(map(str, arr)))

# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Best for educational purposes and small datasets. Not efficient for large or nearly sorted datasets.
# Use for learning only.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Suitable for small datasets. It minimizes the number of swaps.
# Use when you want a simple sorting algorithm for small lists.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Good for small datasets and nearly sorted lists.
# Use when the dataset is small or mostly sorted.

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Efficient for large datasets. Stable sorting algorithm (keeps order for duplicates).
# Use when you need a reliable, stable, efficient sorting algorithm for large datasets (slightly faster then heap sort but requires extra space).

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Quick Sort
# Time Complexity: O(n^2) worst case, O(n log n) average case
# Space Complexity: O(log n) average, O(n) worst case (for call stack)
# Efficient for large datasets. Fast and widely used in practice. Not inherintly stable.
# Time Complexity can vary; often has the fastest average time complexity.
# Use when you need a fast, unstable sorting algorithm for large datasets.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Heap Sort
# Time Complexity: O(n log n)
# Space Complexity: O(1) (in-place sorting)
# Efficient for large datasets. In-place sorting with a stable worst-case performance.
# Suitable for situations where stable sorting is not required.
# Use when you need an efficient, stable, in-place sorting algorithm for large datasets with no extra space.

def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Test list for sorting
test_list = random.sample(range(1, 101), 10)  # Randomly generated list of 10 integers

# Test and print unsorted list
print("Unsorted List:", test_list)

# Test and measure execution time for each sorting algorithm using timeit
algorithm_names = [
    "Bubble Sort (Small Dataset)",
    "Selection Sort (Small Dataset)",
    "Insertion Sort (Small Dataset)",
    "Merge Sort (Large Dataset)",
    "Quick Sort (Large Dataset)",
    "Heap Sort (Large Dataset)",
]
algorithms = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort,
]

for name, algorithm in zip(algorithm_names, algorithms):
    test_list_copy = test_list.copy()
    time_taken = timeit.timeit(lambda: algorithm(test_list_copy), number=10000)
    print(name + ":")
    print("Sorted List:", test_list_copy)
    print("Time taken:", round(time_taken, 6), "seconds")
    print()