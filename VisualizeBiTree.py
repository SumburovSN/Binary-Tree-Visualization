import matplotlib
from matplotlib import pyplot as plt, patches
from BiTree import BiTree


def show(tree):
    radius = 0.5
    base_step = 2 * radius

    plt.rcParams["figure.figsize"] = [10.00, 7.00]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot(111)

    max_level = BiTree.get_level(tree.get_last(tree.root))

    for floor in range(max_level + 1):
        level = max_level - floor
        y = (max_level - level) * 2
        offset = base_step / 2 + pow(2, (max_level - level - 1)) - 1
        step = pow(2, max_level - level)
        for n in range(pow(2, level)):
            x = offset + step * n
            circle = matplotlib.patches.Circle((x, y), radius=radius, edgecolor='grey', fill=False)
            ax.add_patch(circle)

    def add_node(node):
        def get_serial_parent(child_serial):
            if child_serial == 0:
                return None
            if child_serial % 2 == 1:
                return (child_serial - 1) / 2
            else:
                return (child_serial - 2) / 2

        def get_x(serial, depth):
            level = BiTree.get_level(serial)
            offset = base_step / 2 + pow(2, (depth - level - 1)) - 1
            step = pow(2, depth - level)
            coord_x = offset + step * BiTree.get_serial_in_level(serial)
            return coord_x

        def get_y(serial, depth):
            level = BiTree.get_level(serial)
            y = (depth - level) * 2
            return y

        x = get_x(node.serial, max_level)
        y = get_y(node.serial, max_level)
        parent = get_serial_parent(node.serial)
        if parent is not None:
            parent_x = get_x(parent, max_level)
            parent_y = get_y(parent, max_level)
            arrow = matplotlib.patches.Arrow(parent_x, parent_y, x - parent_x, y - parent_y, width=.1)
            ax.add_patch(arrow)
        circle = matplotlib.patches.Circle((x, y), radius=radius, edgecolor='magenta', fill=False)
        ax.add_patch(circle)
        text = str(node.value)
        # text = str(node.serial) + ": " + str(node.value)
        ax.text(x, y, text, fontsize=7)

    tree.preorder(tree.root, add_node)

    # plt.xlim([0, 8])
    # plt.ylim([0, 8])
    plt.axis('equal')
    plt.axis('off')
    plt.show()


# if __name__ == '__main__':
#     sample_size = 127
#     initial = []
#     for element in range(sample_size):
#         initial.append(element)
#
#     array = []
#     BiTree.get_middle(0, len(initial) - 1, array)
#
#     test_tree = BiTree()
#     for item in array:
#         test_tree.build(item)
#
#     array = []
#     test_tree.get_array(test_tree.root, array, 'preorder')
#     print(array)
#
#     print('last: {}'.format(test_tree.get_last(test_tree.root)))
#     show(test_tree)
