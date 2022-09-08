class Queue:
    """
    Queue is an example of a data structure that can accumulate elements by usage of the enqueue() method
    and return its element due to FIFO (first input - first output) rule with the aid of the dequeue() method.
    The size() method is optional.
    The Queue class has an inner class Node that contains its value and the reference to the following Node.
    """

    class Node:
        def __init__(self, value=None):
            self.value = value
            self.following = None

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        self.cursor = None

    def __len__(self):
        return self.length

    def __str__(self):
        return "The Queue with the size {}. The first element is {}, the last element is {}".\
            format(self.length, self.first.value, self.last.value)

    def __iter__(self):
        self.cursor = self.first
        return self

    def __next__(self):
        if self.cursor:
            value = self.cursor.value
            self.cursor = self.cursor.following
            return value
        else:
            raise StopIteration

    def enqueue(self, value):
        if self.first is None:
            self.first = Queue.Node(value)
            self.last = self.first
        else:
            new = Queue.Node(value)
            self.last.following = new
            self.last = new
        self.length += 1

    def dequeue(self):
        if self.first is None:
            return False
        else:
            gift = self.first.value
            self.first = self.first.following
            self.length -= 1
            return gift
