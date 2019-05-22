from test_framework import generic_test
from heapq import heappushpop, heappush, heappop

def online_median(sequence):
    # TODO - you fill in here.
    min_heap=[]
    max_heap=[]
    ret = []
    for x in sequence:
        heappush(min_heap, -heappushpop(max_heap, -x))

        if len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))
        ret.append(0.5*(min_heap[0]-max_heap[0]) if len(min_heap)==len(max_heap) else -max_heap[0]) 
    return ret

def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
