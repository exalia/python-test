class Node:
    def __init__(self, val):
        #self.left = None # is a Node
        #self.right = None # is a Node
        self.next = None
        self.value = val

class tree:
    def __init__(self, first):
        self.first_node = first

    def add(self, new_node):
        node = self.first_node
        while node.next is not None:
            node = next.next
        node.next = new_node

    def print_tree(self):
        tmp = self.first_node
        while tmp != None:
            print (tmp.value)
            tmp = tmp.next

    def search_value(self, val):
        tmp = self.first_node
        while tmp != None:
            if tmp.value == val:
                return True
            tmp = tmp.next
        return False

def get_classes():
    li = [tree]
    return li
