from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    # TODO - you fill in here.
    i, j = m-1, n-1
    
    while i>=0 or j>=0:
        if (j==-1) or (i >= 0 and A[i] >= B[j]):
            A[i+j+1] = A[i]
            i -= 1

        else:
            A[i+j+1] = B[j]
            j -= 1


    

def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
