from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BFS (Breadth-First Search)
def bfs(root):
    if root:
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            print(node.value, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Iterative Preorder Traversal
def preorder_iterative_dfs(root):
    if root:
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            print(node.value, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

# Iterative Inorder Traversal
def inorder_iterative_dfs(root):
    if root:
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            print(node.value, end=" ")
            root = node.right

# Iterative Postorder Traversal
def postorder_iterative_dfs(root):
    if root:
        stack = []
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            node = stack[-1]

            if not node.right or node.right == prev:
                print(node.value, end=" ")
                prev = stack.pop()
            else:
                root = node.right

# Recursive Preorder Traversal
def preorder_recursive_dfs(root):
    if root:
        print(root.value, end=" ")
        preorder_recursive_dfs(root.left)
        preorder_recursive_dfs(root.right)

# Recursive Inorder Traversal
def inorder_recursive_dfs(root):
    if root:
        inorder_recursive_dfs(root.left)
        print(root.value, end=" ")
        inorder_recursive_dfs(root.right)

# Recursive Postorder Traversal
def postorder_recursive_dfs(root):
    if root:
        postorder_recursive_dfs(root.left)
        postorder_recursive_dfs(root.right)
        print(root.value, end=" ")

# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Test the traversals
print("BFS:")
bfs(root)

print("\nIterative Preorder DFS:")
preorder_iterative_dfs(root)

print("\nIterative Inorder DFS:")
inorder_iterative_dfs(root)

print("\nIterative Postorder DFS:")
postorder_iterative_dfs(root)

print("\nRecursive Preorder DFS:")
preorder_recursive_dfs(root)

print("\nRecursive Inorder DFS:")
inorder_recursive_dfs(root)

print("\nRecursive Postorder DFS:")
postorder_recursive_dfs(root)