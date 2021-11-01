class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# check if the the tree includes node whose value equals target
def tree_includes(root, target):
    if root == None:
        return False
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.data == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False


def tree_includes_recursion(root, target):
    if root == None:
        return False
    # 这里绝对不能写 不相等的情况 因为 如果遇到打他不等于target就直接return falsee的话他的左右子节点就不会去进入recursion了
    if root.data == target:
        return True
    return tree_includes_recursion(root.left, target) or tree_includes_recursion(
        root.right, target
    )


# testcase 00
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(tree_includes(a, "e"))  # -> True
print(tree_includes_recursion(a, "3"))

# test case 01
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
print(tree_includes(a, "a"))  # -> True
print(tree_includes_recursion(a, "a"))

# test case 02
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(tree_includes(a, "n"))  # -> False

