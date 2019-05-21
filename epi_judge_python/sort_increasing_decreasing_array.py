from test_framework import generic_test
import heapq

def sort_k_increasing_decreasing_array(A):
    # TODO - you fill in here.
    L = [] #list of start elements
    i = 0
    L.append(i)
    while i <= len(A): # for every elements in A
        while i+1<len(A) and A[i] <= A[i+1]: # while el of A are increasing (non decreasing actually)
            i += 1
        if i+1 > len(A):
            break
        i += 1 # start of next inc/dec seq
        L.append(i)

        while i+1<len(A) and A[i] >= A[i+1]: #while el in A are decreasing (non increasing actually)
            i += 1
        if i+1 > len(A):
            break
        i += 1
        L.append(i)

    if i != len(A):
        L.append(len(A))
    
    for idx, el in enumerate(L):
        if idx+1 < len(L) and idx%2==1:
            A[el: L[idx+1]] = A[el:L[idx+1]][::-1]
    H = [(A[L[i]], L[i], L[i+1]) for i in range(len(L)-1)]
    heapq.heapify(H)
    ret =[]
    while H:
        val, i, end = heapq.heappop(H)
        ret.append(val)
        if i+1 < end:
            heapq.heappush(H, (A[i+1], i+1, end))
    return ret





    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
