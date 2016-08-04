class Node:
    def __init__(self, val):
        self.left = None # is a Node
        self.right = None # is a Node
        self.value = val

class tree:
    def __init__(self):
        self.first_node = None

    # Add node

    def add(self, val):
        if self.first_node == None:
            self.first_node = Node(val)
        else:
            self.add_recursive(val, self.first_node)

    def add_recursive(self, val, node):
        if val < node.value:
            if node.left != None:
                self.add_recursive(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right != None:
                self.add_recursive(val, node.right)
            else:
                node.right = Node(val)

    # Search tree Value

    def run(self, val):
        if self.first_node != None:
            return False if self.get_node_by_value(val, self.first_node) == None else True
        else:
            return False

    def get_node_by_value(self, val, node):
        if val == node.value:
            return node
        elif val < node.value and node.left != None:
            return self.get_node_by_value(val, node.left)
        elif val > node.value and node.right != None:
            return self.get_node_by_value(val, node.right)

    # print tree

    def print_all_values(self):
        if self.first_node != None:
            self.print_recursive(self.first_node)

    def print_recursive(self, node):
        if(node != None):
            self.print_recursive(node.left)
            print (str(node.value))
            self.print_recursive(node.right)


def get_classes():
    li = [tree]
    return li

tree = tree()
tree.add(47)
tree.add(79)
tree.print_all_values()
print (tree.run(79))
print (tree.run(34))
