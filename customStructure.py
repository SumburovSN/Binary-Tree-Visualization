from Stack import Stack
from Queue import Queue
from BiTree import BiTree
from VisualizeBiTree import show


def example1_stack():
    test_stack = Stack()

    for step in range(10):
        initial = ord('a')
        item = chr(initial + step)
        test_stack.push(item)

    print(len(test_stack))
    print(test_stack)
    print(test_stack.first)
    print(test_stack.first.value)
    print(test_stack.first.following)
    print(test_stack.first.following.value)
    print(test_stack.first.following.following.value)

    print(test_stack.pop())
    print(test_stack.pop())

    print(len(test_stack))

    for element in test_stack:
        print("Element: {}".format(element))

    print(test_stack)


def example2_queue():
    test_queue = Queue()

    for step in range(10):
        initial = ord('a')
        item = chr(initial + step)
        test_queue.enqueue(item)

    print(len(test_queue))

    print(test_queue.dequeue())
    print(len(test_queue))

    print(test_queue.dequeue())
    print(len(test_queue))

    for element in test_queue:
        print("Element: {}".format(element))

    print(test_queue)


def example3_comparison_stack_queue():
    test_stack = Stack()
    test_queue = Queue()

    for step in range(10):
        initial = ord('a')
        item = chr(initial + step)
        test_stack.push(item)

    info = ''
    for i in range(10):
        info += test_stack.pop() + ' '
    print(info)

    for step in range(10):
        initial = ord('a')
        item = chr(initial + step)
        test_queue.enqueue(item)

    info = ''
    for i in range(10):
        info += test_queue.dequeue() + ' '
    print(info)


def example4_bi_tree():
    test_tree = BiTree()

    unsorted = [4, 3, 5, 2, 7, 8, 1, 9, 0]
    for item in unsorted:
        test_tree.build(item)

    print(test_tree.build_array_tree())

    test_tree2 = BiTree()
    unsorted = [5, 3, 7, 2, 4, 6, 8, 0, 9]
    for item in unsorted:
        test_tree2.build(item)

    print(test_tree2.build_array_tree())


def example5_bi_tree(size):
    array = []
    BiTree.get_middle(0, size - 1, array)

    print(array)

    test_tree = BiTree()

    for item in array:
        test_tree.build(item)

    print(test_tree)

    # levels = {}
    # test_tree.get_map_levels(test_tree.root, levels, 'descending')
    # print(levels)
    #
    levels = {}
    test_tree.get_map_levels(test_tree.root, levels, 'postorder')
    print(levels)

    # array = []
    # test_tree.get_array(test_tree.root, array, 'descending')
    # print(array)
    #
    # array = []
    # test_tree.get_array(test_tree.root, array)
    # print(array)
    #
    # array = []
    # test_tree.get_array(test_tree.root, array, 'postorder')
    # print(array)

    array = []
    test_tree.get_array(test_tree.root, array, 'preorder')
    print(array)

    test_tree.inorder_descending(test_tree.root.left.right)

    print(test_tree.build_array_tree())

    parent, node = test_tree.find(test_tree.root, 10)
    print(parent, node)


def example6_visualize(size):
    array = []
    BiTree.get_middle(0, size - 1, array)

    test_tree = BiTree()
    for item in array:
        test_tree.build(item)

    array = []
    test_tree.get_array(test_tree.root, array, 'preorder')
    print(array)

    print('last: {}'.format(test_tree.get_last(test_tree.root)))
    show(test_tree)

    # test_tree.remove(27)
    # show(test_tree)
    #
    # test_tree.remove(31)
    # show(test_tree)

    print(test_tree.remove(64))
    show(test_tree)


# test creating balanced tree based on random
def example7_bi_tree(size):
    test_tree = BiTree.populating_bi_tree(size, "symbols")
    array = []
    test_tree.get_array(test_tree.root, array)
    print(array)

    test_tree.balance_tree()
    # check balance on the elements count in each level
    levels = {}
    test_tree.get_map_levels(test_tree.root, levels)
    print(levels)
    show(test_tree)


if __name__ == '__main__':
    # the Stack
    # example1_stack()

    # the Queue
    # example2_queue()

    # a comparison between the stack and the queue
    # example3_comparison_stack_queue()

    # the tree
    # example4_bi_tree()

    example5_bi_tree(127)

    # example6_visualize(63)

    # example7_bi_tree(31)
    # print(ord('А'), ord('я'), ord('!'), ord('a'), ord('A'), ord('0'))
    # word = ""
    # for i in range(130):
    #     word += chr(i+1040)
    # print(word)

    # class MyNumbers:
    #     def __iter__(self):
    #         self.a = 1
    #         return self
    #
    #     def __next__(self):
    #         if self.a <= 20:
    #             x = self.a
    #             self.a += 1
    #             return x
    #         else:
    #             raise StopIteration
    #
    #
    # myclass = MyNumbers()
    # myiter = iter(myclass)
    # for x in myiter:
    #     print(x)

