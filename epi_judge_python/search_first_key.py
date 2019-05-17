from test_framework import generic_test


def search_first_of_k(A, k):
    # TODO - you fill in here.
    L, U = 0, len(A)-1

    while L <= U:
        M = L + (U-L)//2
        if A[M] < k:
            L = M+1
        elif A[M] > k:
            U = M-1
        elif M==0 or A[M-1]!=k:
            return M
        else:
            U = M-1

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
