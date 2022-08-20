import math
from random import randint


class BiTree:
    """
    BiTree (Binary Tree) is an example of a data structure that can accumulate elements while sorting them with the aid
    of the add() method.
    The size() method is optional.
    The BiTree class has an inner class Node that contains its value and the reference to 2 children (left and right).
    The property 'level' is optional.
    TO-DO: implement the remove() method.
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
        self.last = 0
        self.data_structure = None
        self.found = None, None

    def __len__(self):
        return self.length

    def build(self, value):
        if self.root is None:
            self.root = BiTree.Node(value, 0)
            self.length += 1
        else:
            self.add(self.root, value)

    def add(self, node, value):
        if node.value > value:
            if node.left is None:
                node.left = BiTree.Node(value, node.serial * 2 + 1)
                self.length += 1
            else:
                self.add(node.left, value)
        elif node.value < value:
            if node.right is None:
                node.right = BiTree.Node(value, node.serial * 2 + 2)
                self.length += 1
            else:
                self.add(node.right, value)
        else:
            print("The value {} exists already.".format(value))

    def get_last(self, node):
        if node is None:
            return
        else:
            self.get_last(node.left)
            if self.last < node.serial:
                self.last = node.serial
            self.get_last(node.right)
        return self.last

    # @staticmethod
    # def get_deepest(start_node, direction="left"):
    #     depth = 0
    #     parent = leaf = start_node
    #     if direction == "left":
    #         node = start_node.left
    #     else:
    #         node = start_node.right
    #     while node:
    #         parent = leaf
    #         leaf = node
    #         depth += 1
    #         if direction == "left":
    #             node = node.right
    #         else:
    #             node = node.left
    #     return leaf, parent, depth

    # def get_leftmost(self, node, depth):
    #     if node.left:
    #         self.get_leftmost(node.left, depth + 1)
    #     else:
    #         print("The Leftmost' value: {}, depth: {}".format(node.value, depth))
    #         return node, depth
    #
    # def get_rightmost(self, node, depth):
    #     if node.right:
    #         self.get_rightmost(node.right, depth + 1)
    #     else:
    #         print("The Rightmost' value: {}, depth: {}".format(node.value, depth))
    #         return node, depth

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

    def build_array_tree(self):
        def add_in_array_tree(node):
            self.data_structure[node.serial] = node.value

        self.get_last(self.root)
        self.data_structure = [None] * (self.last + 1)
        self.preorder(self.root, add_in_array_tree)
        return self.data_structure

    def get_array(self, node, array, traverse_type='ascending'):
        def append_node(node):
            # self.data_structure.append(node.value)
            self.data_structure.append(str(node.value) + ', serial: ' + str(node.serial))

        self.data_structure = array
        if traverse_type == 'ascending':
            self.inorder_ascending(node, append_node)
        elif traverse_type == 'descending':
            self.inorder_descending(node, append_node)
        elif traverse_type == 'preorder':
            self.preorder(node, append_node)
        else:
            self.postorder(node, append_node)

    def get_map_levels(self, node, dictionary, traverse_type='ascending'):
        def calculate_level(node):
            return math.floor(math.log2(node.serial + 1))

        def update_map(node):
            level = calculate_level(node)
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

    @staticmethod
    def get_level(serial):
        return math.floor(math.log2(serial + 1))

    @staticmethod
    def get_serial_in_level(serial):
        return serial - math.floor(math.pow(2, BiTree.get_level(serial))) + 1

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
    def populating_bi_tree(sample_size):
        sample = []
        initial = []
        for element in range(sample_size):
            initial.append(element)

        # populating the sample from the initial in random sequence
        while initial:
            element = initial.pop(randint(0, len(initial) - 1))
            sample.append(element)

        return sample

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
