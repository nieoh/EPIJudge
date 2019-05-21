from test_framework import generic_test
import heapq

def sort_approximately_sorted_array(sequence, k):
    # TODO - you fill in here.
    i = 0
    H = []
    ret=[]
    while i < k:
        H.append(next(sequence))
        i+=1
    heapq.heapify(H)
    while H:
        el = heapq.heappop(H)
        ret.append(el)
        try:
            heapq.heappush(H, next(sequence))
        except StopIteration:
            continue

    return ret


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
