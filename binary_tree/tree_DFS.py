class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# this is a preorder DFS using a stack and will append right node in to stack first
def depth_first_values(root):
    stack = [root]
    result = []
    while len(stack) > 0:
        current = stack.pop()
        result.append(current)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result


# This method has some problems on th last return because the return value is
# a
# ['b', ['d', [], []], ['e', [], []]]
# ['c', [], ['f', [], []]]
def depth_first_values_recursion(root):
    if root == None:
        return []
    left_values = depth_first_values_recursion(root.left)
    right_values = depth_first_values_recursion(root.right)
    return [root.data] + [left_values] + [right_values]
