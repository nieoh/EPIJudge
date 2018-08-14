from test_framework import generic_test, test_utils

def reverse_order_traversal(tree):
    if tree is None:
        return []

    r = reverse_order_traversal(tree.right)
    for node in r:
        yield node
    yield tree
    l = reverse_order_traversal(tree.left)
    for node in l:
        yield node

def find_k_largest_in_bst(tree, k):
    ret = [] 
    for node in reverse_order_traversal(tree):
        if node:
            ret.append(node.data)
        k -= 1
        if 0 == k:
            break
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
