from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    # TODO - you fill in here.
    if len(A) > len(B):
        A, B = B, A
    dict = {}
    ret = []

    for a in A:
        if a not in dict:
            dict[a] = 0


    for b in B:
        if b in dict:
            dict[b] = 1
    for key, val in dict.items():
        if val > 0:
            ret.append(key)


    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
