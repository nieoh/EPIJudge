from test_framework import generic_test


def find_nearest_repetition(paragraph):
    dic = {}
    nearest = len(paragraph)
    for idx, word in enumerate(paragraph):
        if word in dic:
            nearest = min(nearest, idx-dic[word])
        dic[word] = idx
        
    return -1 if nearest == len(paragraph) else nearest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
