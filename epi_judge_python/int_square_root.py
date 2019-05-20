from test_framework import generic_test


def square_root(k):
    # TODO - you fill in here.
    if k == 0:
        return 0
    if k <= 3:
        return 1
    L, U = 1, k//2
    while L<=U:
        M = L + (U-L)//2
        if M**2 == k:
            return M
        elif M**2 > k:
            U = M-1
        elif (M+1)**2 > k:
            return M
        else:
            L = M+1



    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
