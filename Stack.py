class Stack:
    """
    Stack is an example of a data structure that can accumulate elements by usage of the push() method
    and return its element due to LIFO (last input - first output) rule with the aid of the pop() method.
    The size() method is optional.
    The Stack class has an inner class Node that contains its value and the reference to the following Node.
    """

    class Node:
        def __init__(self, value=None, following=None):
            self.value = value
            self.following = following

    def __init__(self):
        self.first = None
        self.length = 0

    def __str__(self):
        return "The Stack with the size {}. The first element is {}".format(self.length, self.first.value)

    def push(self, value):
        if self.first is None:
            self.first = Stack.Node(value)
        else:
            new = Stack.Node(value, self.first)
            self.first = new
        self.length += 1

    def pop(self):
        if self.first is None:
            return False
        else:
            gift = self.first.value
            self.first = self.first.following
            self.length -= 1
            return gift

    def size(self):
        return self.length

