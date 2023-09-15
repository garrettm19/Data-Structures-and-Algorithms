# Lists: Lists are ordered collections of items that can be of any data type. They are mutable, meaning you can modify their contents.

my_list = [1, 2, 3]

# Tuples: Tuples are similar to lists but are immutable, meaning their elements cannot be changed after creation. They are often used to represent fixed collections of items.

my_tuple = (1, 2, 3)

# Dictionaries: Dictionaries are unordered collections of key-value pairs. They are used to store and retrieve data using a unique key. Keys must be immutable.

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Sets: Sets are unordered collections of unique elements. They are useful for tasks that require unique values or testing membership.

my_set = {1, 2, 3, 2, 1}  # Duplicates are automatically removed

# Arrays: Arrays are available through the array module and are more memory-efficient than lists when dealing with homogeneous data types.

import array

my_array = array.array('i', [1, 2, 3])  # 'i' represents integer type

# Hash Tables: Dictionaries in Python are examples of hash tables.

my_dict = {'name': 'Alice', 'age': 25}
empty_dict2 = dict()

from collections import defaultdict
empty_default_dict = defaultdict(list)  # Default value is an empty list

# Hash Sets: Sets in Python are examples of hash sets.

my_set = {1, 2, 3}
empty_set = set()

# Stacks: You can implement a stack using a list.

my_stack = []
my_stack.append(1)
my_stack.append(2)
my_stack.pop()  # Returns 2 (Last-In-First-Out)

# Queues: You can implement a queue using the queue module.

from queue import Queue

my_queue = Queue()
my_queue.put(1)
my_queue.put(2)
my_queue.get()  # Returns 1 (First-In-First-Out)

# Deque: Deques can be used to add and remove elements from both ends efficiently.

from collections import deque

my_deque = deque([1, 2, 3])
my_deque.appendleft(0)
my_deque.pop()  # Returns 3
my_deque.popleft()  # Returns 0

# Linked Lists: Linked lists require a custom implementation but are commonly used for tasks involving efficient insertions and deletions.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# Trees: Trees are hierarchical data structures. Here's an example of a binary tree:

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Heaps: You can use the heapq module for heaps. Here's an example of a min heap:

import heapq

my_heap = []
heapq.heappush(my_heap, 3)
heapq.heappush(my_heap, 1)
heapq.heappush(my_heap, 2)

# Priority Queues: You can use the queue.PriorityQueue class for priority queues.

from queue import PriorityQueue

my_priority_queue = PriorityQueue()
my_priority_queue.put((1, 'Task 1'))
my_priority_queue.put((3, 'Task 3'))
my_priority_queue.put((2, 'Task 2'))

# Graphs: Graphs require custom implementations for specific use cases. They consist of nodes connected by edges, representing relationships.