import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def construct_ancestor(tree, node):
    ret = [tree]
    if not tree:
        return []
    if tree.data == node.data:
        return ret
    elif tree.data < node.data:
        return ret+construct_ancestor(tree.right, node)
    else:
        return ret+construct_ancestor(tree.left, node)

# Input nodes are nonempty and the key at s is less than or equal to that at b.
def find_LCA(tree, s, b):
    # TODO - you fill in here.
    ancestor1 = construct_ancestor(tree, s)
    ancestor2 = construct_ancestor(tree, b)
    i = 1
    while i < min(len(ancestor1), len(ancestor2)) and ancestor1[i].data == ancestor2[i].data:
        i += 1
     
    return ancestor1[i-1]


@enable_executor_hook
def lca_wrapper(executor, tree, s, b):
    result = executor.run(
        functools.partial(find_LCA, tree, must_find_node(tree, s),
                          must_find_node(tree, b)))
    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_in_bst.py",
                                       'lowest_common_ancestor_in_bst.tsv',
                                       lca_wrapper))
