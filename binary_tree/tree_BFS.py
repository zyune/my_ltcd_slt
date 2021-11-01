class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def breadthfirstvalues(root):
    if root == None:
        return []
    values = []
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        values.append(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return values


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
print(breadthfirstvalues(a))
# test case 02
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h


print(breadthfirstvalues(a))
# 在python中 [ ] pop()方法默认pop出最右边的那个。如果要pop出最左边的用pop(0)
# array = ["a", "b", "c"]
# array.append("fashdjko")
# array.pop(0)
# print(array)

