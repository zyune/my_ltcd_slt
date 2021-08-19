class Node:
    #https://realpython.com/linked-lists-python/#how-to-create-a-linked-list
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next   
    def add_first(self, node):
        node.next = self.head
        self.head = node
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
    
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
    
        raise Exception("Node with data '%s' not found" % target_node_data)
    
llist=LinkedList()
firstnode=Node("a")
llist.head=firstnode
secondnode=Node("b")
firstnode.next=secondnode
llist
print(llist)