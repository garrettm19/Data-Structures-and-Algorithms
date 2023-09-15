import random

# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found

# Test list for binary search
test_list = sorted(random.sample(range(1, 101), 10))  # Sorted list of 10 integers
target = random.randint(1, 100)  # Random target value

# Print the test case
print("Test List:", test_list)
print("Target:", target)

# Perform binary search
result = binary_search(test_list, target)

# Print the result
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")
