
# Dynamic Programming

# Fibonacci Sequence (Recursive)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Recursion

# Factorial (Recursive)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# Greedy Algorithms

# Coin Change (Greedy)
def coin_change(coins, amount):
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            num_coins += 1
    return num_coins

# Backtracking

# Suduko Board Problem
def solve_sudoku(board):
    # Find an empty cell (cell with value 0)
    empty_cell = find_empty_cell(board)
    
    # If there are no empty cells, the Sudoku is solved
    if not empty_cell:
        return True
    
    row, col = empty_cell
    
    # Try filling the empty cell with numbers from 1 to 9
    for num in range(1, 10):
        if is_valid_move(board, num, (row, col)):
            board[row][col] = num
            
            # Recursively attempt to solve the rest of the Sudoku
            if solve_sudoku(board):
                return True
            
            # If the current placement does not lead to a solution, backtrack
            board[row][col] = 0
    
    # If no valid number can be placed in the current cell, backtrack
    return False

def find_empty_cell(board):
    # Find the first empty cell (cell with value 0)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None  # If there are no empty cells, the Sudoku is solved

def is_valid_move(board, num, position):
    # Check if 'num' is a valid move in the current position (row, col)
    row, col = position
    
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Sudoku Solved:")
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists.")

# Two-Pointers Technique

# Two Sum (Two-Pointers)
def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []  # No solution found

# Sliding Window Technique

# Maximum Subarray Sum (Sliding Window)
def max_subarray_sum(nums, k):
    max_sum = curr_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum

# Bit Manipulation

# Count Set Bits
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Divide and Conquer

# Power Function (Divide and Conquer)
def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x

# Topological Sorting

# Course Schedule Problem
from collections import defaultdict

def can_finish(num_courses, prerequisites):
    # Create a graph to represent the courses and their dependencies
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    # Populate the graph and in-degree array
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Initialize a queue to perform topological sorting
    queue = []
    for course in range(num_courses):
        if in_degree[course] == 0:
            queue.append(course)

    # Perform topological sorting
    while queue:
        course = queue.pop(0)
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if all courses can be finished (no cycles)
    return sum(in_degree) == 0

# Example usage:
num_courses = 4
prerequisites = [[1,0],[2,1],[3,2]]
result = can_finish(num_courses, prerequisites)
print(result)  # Output: True (Courses can be finished in the specified order)


# Union-Find (Disjoint Set)
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1