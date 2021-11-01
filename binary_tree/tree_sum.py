class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def tree_sum_recursion(root):
    if root == None:
        return 0
    return root.data + tree_sum_recursion(root.left) + tree_sum_recursion(root.right)


def tree_sum_mycode(root):
    if root == None:
        return 0
    left_value = tree_sum_mycode(root.left)
    right_value = tree_sum_mycode(root.right)
    return root.data + left_value + right_value


def tree_sum_iteration(root):
    if root == None:
        return 0
    queue = [root]
    sum_value = 0
    while len(queue) > 0:
        current = queue.pop(0)
        sum_value += current.data
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return sum_value


# test case 0
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
print(tree_sum_recursion(a))
print(tree_sum_iteration(a))

# test case 01
a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

print(tree_sum_recursion(a))  # -> 10
print(tree_sum_mycode(a))
print(tree_sum_iteration(a))

# test case 03
print(tree_sum_recursion(None))  # -> 0
print(tree_sum_mycode(None))

