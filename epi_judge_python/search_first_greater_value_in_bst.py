from test_framework import generic_test

def find_min_value(tree):
    if tree.left is None:
        return tree
    return find_min_value(tree.left)

def find_first_greater_than_k(tree, k):
    if tree is None or tree.data is None:
        return None
    if tree.data > k:
        if tree.left is None:
            return tree
        return find_first_greater_than_k(tree.left, k)
    if tree.data < k:
        if tree.right is None:
            if tree.parent is None:
                return None
            while tree.parent is not None and tree.parent.data < k:
                tree = tree.parent
            return tree.parent
        return find_first_greater_than_k(tree.right, k)
    if tree.data == k:
        if tree.right is None:
            if tree.parent is None:
                return None
            while tree.parent is not None and tree.parent.data < k:
                tree = tree.parent
            return tree.parent
        return find_min_value(tree.right)
    
    return None


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
