from test_framework import generic_test, test_utils

def reverse_traversal(tree):
    if not tree:
        return []

    for x in reverse_traversal(tree.right):
        yield x

    yield tree.data

    for y in reverse_traversal(tree.left):
        yield y


def find_k_largest_in_bst(tree, k):
    ret = []

    for node in reverse_traversal(tree):
        if node:
            ret.append(node)
        k -= 1
        if k == 0:
            break

    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
