import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from doubly_list_node import DoublyListNode

def bst_to_doubly_linked_list(tree):
    def helper(tree):
        if not tree:
            return None, None
        l = DoublyListNode(tree.data)
        first = last = l
        F, l.prev = helper(tree.left)
        if l.prev:
            l.prev.next = l
        if F:
            first = F
        l.next , L = helper(tree.right)
        if l.next:
            l.next.prev = l
        if L:
            last = L

        return first, last

    head, _ = helper(tree)
    return head

@enable_executor_hook
def bst_to_doubly_linked_list_wrapper(executor, tree):
    l = executor.run(functools.partial(bst_to_doubly_linked_list, tree))
    if l is not None and l.prev is not None:
        raise TestFailure(
            'Function must return the head of the list. Left link must be None'
        )
    v = []
    while l:
        v.append(l.data)
        if l.next and l.next.prev is not l:
            raise TestFailure('List is ill-formed')
        l = l.next
    return v


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_to_sorted_list.py",
                                       'bst_to_sorted_list.tsv',
                                       bst_to_doubly_linked_list_wrapper))
