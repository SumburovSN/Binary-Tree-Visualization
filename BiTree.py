import math
from random import randint


class BiTree:
    """
    BiTree (Binary Tree) is an example of a data structure that can accumulate elements while sorting them with the aid
    of the build() method.
    The length property is optional.
    Each element is an instance of the inner Node class. Traditionally, each node contains the value and references to
    the left and right children.

    The 'serial' property (serial number) has been added in order:
    (1) to convert a binary tree represented by nodes into the binary tree based on an array. Array methods haven't been
    implemented
    (2) to calculate the node coordinates to visualize the tree with the aid of show() of VisualizeBiTree.py.
        About node's serial number:
        Serial of the left children = Parent's serial * 2 + 1
        Serial of the right children = Parent's serial * 2 + 2
        Max amount of nodes for nth level = 2^n - 1 (geometric progression sum)
        The node's level = floor(log2(node serial + 1)). It is calculated by get_level() method.
        The serial number of the node in its level = node's serial - 2^(node's level) + 1. It is calculated by
        get_serial_in_level() method.

    BiTree has usual traversing methods such as preorder, postorder. The inorder method has been broken down into
    ascending and descending modes. All the traversal methods can accept a custom visit() callback function as an
    argument. Examples of the callback function are get_array() and get_map_levels() methods return an array and
    a dictionary accordingly.
    BiTree can build a balanced (shallow) binary tree with the aid of get_middle() method that returns indices for
    sorted array to pass into build() method.
    The example of getting a random tree balanced is in balance_tree() method.
    """

    class Node:
        def __init__(self, value, serial=None):
            self.value = value
            self.serial = serial
            self.left = None
            self.right = None

        def __str__(self):
            return str(self.serial) + ". " + str(self.value)

    def __init__(self):
        self.root = None
        self.length = 0
        # last 3 properties are designed to hold references in the recursive functions
        self.last = 0
        self.data_structure = None
        self.found = None, None

    def __len__(self):
        return self.length

    def __str__(self):
        return "The Binary Tree with the size {}. The root element is {}".format(self.length, self.root.value)

    # method to add the value into the tree
    def build(self, value):
        def add(node, value):
            if node.value > value:
                if node.left is None:
                    node.left = BiTree.Node(value, node.serial * 2 + 1)
                    # print(node.left.serial, node.left.value, node.serial, node.value)
                    self.length += 1
                else:
                    add(node.left, value)
            elif node.value < value:
                if node.right is None:
                    node.right = BiTree.Node(value, node.serial * 2 + 2)
                    # print(node.right.serial, node.right.value, node.serial, node.value)
                    self.length += 1
                else:
                    add(node.right, value)
            else:
                print("The value {} exists already.".format(value))

        if self.root is None:
            self.root = BiTree.Node(value, 0)
            self.length += 1
        else:
            add(self.root, value)

    # returns the largest serial number for visualization
    def get_last(self, node):
        if node is None:
            return
        else:
            self.get_last(node.left)
            if self.last < node.serial:
                self.last = node.serial
            self.get_last(node.right)
        return self.last

    # traversal methods
    def inorder_descending(self, node, visit=print):
        if node is None:
            return
        else:
            self.inorder_descending(node.right, visit)
            visit(node)
            self.inorder_descending(node.left, visit)

    def inorder_ascending(self, node, visit=print):
        if node is None:
            return
        else:
            self.inorder_ascending(node.left, visit)
            visit(node)
            self.inorder_ascending(node.right, visit)

    def postorder(self, node, visit=print):
        if node is None:
            return
        else:
            self.postorder(node.left, visit)
            self.postorder(node.right, visit)
            visit(node)

    def preorder(self, node, visit=print):
        if node is None:
            return
        else:
            visit(node)
            self.preorder(node.left, visit)
            self.preorder(node.right, visit)

    # returns binary tree based on the array
    def build_array_tree(self):
        def add_in_array_tree(node):
            self.data_structure[node.serial] = node.value

        self.get_last(self.root)
        self.data_structure = [None] * (self.last + 1)
        self.preorder(self.root, add_in_array_tree)
        return self.data_structure

    # returns the array of tree's node according to the traversal type
    def get_array(self, node, array, traverse_type='ascending', type='node'):
        def append_node(node):
            if type == 'node':
                self.data_structure.append(str(node.value) + ', serial: ' + str(node.serial))
            else:
                self.data_structure.append(node.value)

        self.data_structure = array
        if traverse_type == 'ascending':
            self.inorder_ascending(node, append_node)
        elif traverse_type == 'descending':
            self.inorder_descending(node, append_node)
        elif traverse_type == 'preorder':
            self.preorder(node, append_node)
        else:
            self.postorder(node, append_node)

    # returns the dictionary of pairs: level -> amount:
    def get_map_levels(self, node, dictionary, traverse_type='ascending'):
        # def calculate_level(node):
        #     return math.floor(math.log2(node.serial + 1))

        def update_map(node):
            level = BiTree.get_level(node.serial)
            if level in self.data_structure.keys():
                self.data_structure[level] += 1
            else:
                self.data_structure.update({level: 1})

        self.data_structure = dictionary
        if traverse_type == 'ascending':
            self.inorder_ascending(node, update_map)
        elif traverse_type == 'descending':
            self.inorder_descending(node, update_map)
        elif traverse_type == 'preorder':
            self.preorder(node, update_map)
        else:
            self.postorder(node, update_map)

    # calculate 'y' coordinate for node with certain serial
    @staticmethod
    def get_level(serial):
        return math.floor(math.log2(serial + 1))

    # calculate 'x' coordinate for node with certain serial
    @staticmethod
    def get_serial_in_level(serial):
        return serial - math.floor(math.pow(2, BiTree.get_level(serial))) + 1

    # binary search with big O notation = log2 N
    def find(self, node, value):
        def compare(node, value, parent):
            if node is None:
                return
            if node.value > value:
                compare(node.left, value, node)
            elif node.value < value:
                compare(node.right, value, node)
            else:
                self.found = node, parent
        self.found = None, None
        compare(node, value, node)
        return self.found

    # if the removing node is leaf just remove the reference to it from the parent node
    # otherwise it seeks the rightmost node from the left subtree and the leftmost node from the right subtree
    # then compares their depth and removes the reference to the deepest node
    # and change the value of the target node to save it serial
    def remove(self, value):
        def get_deepest(start_node, direction="left"):
            depth = 0
            parent = leaf = start_node
            if direction == "left":
                node = start_node.left
            else:
                node = start_node.right
            while node:
                parent = leaf
                leaf = node
                depth += 1
                if direction == "left":
                    node = node.right
                else:
                    node = node.left
            return leaf, parent, depth

        def delete_reference(parent, child):
            if parent.value > child.value:
                parent.left = None
            else:
                parent.right = None

        altering_node, new_parent = self.find(self.root, value)
        if altering_node:
            result = altering_node.value
            left_replacing, left_parent, left_depth = get_deepest(altering_node)
            right_replacing, right_parent, right_depth = get_deepest(altering_node, "right")
            left = True
            if left_depth == right_depth:
                if left_depth == 0:
                    delete_reference(new_parent, altering_node)
                    return result
                else:
                    left = [True, False][randint(0, 1)]
            elif left_depth < right_depth:
                left = False
            if left:
                delete_reference(left_parent, left_replacing)
                altering_node.value = left_replacing.value
            else:
                delete_reference(right_parent, right_replacing)
                altering_node.value = right_replacing.value
            self.length -= 1
            return result

    @staticmethod
    def populating_bi_tree(sample_size, node_type=None):
        # sample = []
        tree = BiTree()
        initial = []

        for element in range(sample_size):
            if node_type is None:
                initial.append(element)
            else:
                initial.append(chr(element + 65))

        # populating the sample from the initial in random sequence
        while initial:
            element = initial.pop(randint(0, len(initial) - 1))
            tree.build(element)

        return tree

    # building an array of indices for balanced tree
    # method can be applied to build balanced tree with integer value's nodes
    @staticmethod
    def get_middle(start, end, array):
        length = end - start + 1
        if length < 1:
            return
        if length == 1:
            array.append(start)
        else:
            if length % 2 == 1:
                middle = int(length / 2) + start
            else:
                middle = randint(int(length/2) - 1, int(length/2)) + start
            array.append(middle)
            BiTree.get_middle(start, middle - 1, array)
            BiTree.get_middle(middle + 1, end, array)

    # create balanced tree from the random one
    def balance_tree(self):
        elements_array = []
        self.get_array(self.root, elements_array, 'ascending', 'value')
        indices_array = []
        BiTree.get_middle(0, len(elements_array) - 1, indices_array)

        built_array = [None] * len(elements_array)

        for i in range(len(elements_array)):
            built_array[i] = elements_array[indices_array[i]]

        self.root = None
        for element in built_array:
            self.build(element)
