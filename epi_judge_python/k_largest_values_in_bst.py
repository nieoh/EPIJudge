from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    if tree is None:
        return []
    ret = []
    
    ret += find_k_largest_in_bst(tree.right, k)
    if len(ret) < k:
        ret.append(tree.data)
    if len(ret) < k:
        ret += find_k_largest_in_bst(tree.left, k-len(ret))
    
    
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
