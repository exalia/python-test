class Node:
    def __init__(self, val):
        self.left = None # is a Node
        self.right = None # is a Node
        self.value = val

class tree:
    def __init__(self):
        self.first_node = None

    # Add node

    def add(self, value):
        if self.first_node == None:
            self.first_node = Node(value)
        else:
            self.add_recursive(value, self.first_node)

    def add_recursive(self, value, node):
        if value > node.value:
            if node.right != None:
                self.add_recursive(value, node.right)
            else:
                node.right = Node(value)
        else:
            if node.left != None:
                self.add_recursive(value, node.left)
            else:
                node.left = Node(value)

    # print tree

    def print_all_values(self):
        if self.first_node != None:
            self.print_recursive(self.first_node)

    def print_recursive(self, node):
        if node != None:
            self.print_recursive(node.left)
            print (node.value)
            self.print_recursive(node.right)

    # Search tree Value

    def run(self, value):
        if self.first_node != None and self.get_node_by_value(value, self.first_node) != None:
            return True
        else:
            return False

    def get_node_by_value(self, value, node):
        if value == node.value:
            return node
        elif value > node.value and node.right != None:
            return self.get_node_by_value(value, node.right)
        elif value < node.value and node.left != None:
            return self.get_node_by_value(value, node.left)


def get_classes():
    return [tree, Node]

tree = tree()
tree.add(47)
tree.add(79)
tree.print_all_values()
print (tree.run(79))
print (tree.run(34))
