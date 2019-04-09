from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    # TODO - you fill in here.
    head = tail = ind = L
    for _ in range(k):
        if ind.next:
            ind = ind.next
        else:
            return head.next
    
    while ind.next:
        tail = tail.next
        ind = ind.next
    tail.next = tail.next.next


    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
