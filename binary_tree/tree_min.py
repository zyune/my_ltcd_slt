class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def tree_min_iteration(root):
    smallest = float("inf")
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        if current.data < smallest:
            smallest = current.data
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return smallest


def tree_min_recursion(root):
    if root == None:
        return float("inf")
    left_min = tree_min_recursion(root.left)
    right_min = tree_min_recursion(root.right)
    return min(root.data, left_min, right_min)


# https://www.w3schools.com/python/ref_func_min.asp
# min(n1, n2, n3, ...)
# a = (1, 5, 3, 9)
# x = min(a)

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
print(tree_min_iteration(a))  # -> -2
print(tree_min_recursion(a))

# test case 01
a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       5
#    /    \
#   11     3
#  / \      \
# 4   15     12

print(tree_min_iteration(a))  # -> 3
print(tree_min_recursion(a))

