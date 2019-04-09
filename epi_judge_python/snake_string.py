from test_framework import generic_test


def snake_string(s):
    # TODO - you fill in here.
    phrase = list(s)
    top = ''
    mid = ''
    bottom = ''
    for i, char in enumerate(phrase):
        if i%4 == 1:
            top+=char
        elif i%2 == 0:
            mid+=char
        else:
            bottom+=char
    return top + mid + bottom


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("snake_string.py", 'snake_string.tsv',
                                       snake_string))
