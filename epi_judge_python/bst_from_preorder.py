from test_framework import generic_test
from binary_tree_node import BinaryTreeNode 

def rebuild_bst_from_preorder(preorder_sequence):
    # TODO - you fill in here.
    if not preorder_sequence:
        return None
    node = preorder_sequence[0]
    i = 1
    while i < len(preorder_sequence) and preorder_sequence[i]<node:
        i += 1
    node = BinaryTreeNode(data=node,
            left=rebuild_bst_from_preorder(preorder_sequence[1:i]),
            right=rebuild_bst_from_preorder(preorder_sequence[i:]))
    return node


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
