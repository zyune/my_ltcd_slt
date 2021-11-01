class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_path_sum_recursion(root):
    if root == None:
        return float("-inf")  # this is negative infinity
    if root.left == None and root.right == None:
        return root.data
    left_path_value = max_path_sum_recursion(root.left)
    right_path_value = max_path_sum_recursion(root.right)
    return root.data + max(left_path_value, right_path_value)


# # Defining a positive infinite integer
# positive_infinity = float('inf')
# print('Positive Infinity: ', positive_infinity)

# # Defining a negative infinite integer
# negative_infinity = float('-inf')
# print('Negative Infinity: ', negative_infinity)


# 这种算法在python中行不通因为会有这种报错
# AttributeError: 'NoneType' object has no attribute 'left'

# def max_path_sum(root):
#     if root.left == None and root.right == None:
#         return root.data
#     max_child_path = max(max_path_sum(root.left), max_path_sum(root.right))
#     return root.data + max_child_path


# test case 00
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(max_path_sum_recursion(a))  # -> 18
# print(max_path_sum(a))
# test case 01
a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3

print(max_path_sum_recursion(a))  # -> 59

# test case 02
a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(0)
f = Node(-13)
g = Node(-1)
h = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   0    -13
#     /       \
#    -1       -2

print(max_path_sum_recursion(a))  # -> -8

# test case 03
a = Node(42)

#        42

print(max_path_sum_recursion(a))  # -> 42

