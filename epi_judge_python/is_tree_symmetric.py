from test_framework import generic_test


def is_symmetric(tree):
    # TODO - you fill in here.
    def func(node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        return (node1.data == node2.data) and (func(node1.left, node2.right)) and (func(node1.right, node2.left))
    if not tree:
        return True
    return func(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
