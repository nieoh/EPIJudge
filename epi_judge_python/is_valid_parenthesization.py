from test_framework import generic_test


def is_well_formed(s):
    # TODO - you fill in here.
    mapping = {'}': '{', ']': '[', ')': '('}

    stack = []

    for char in s:
        if char in mapping:
            if not stack or mapping[char] != stack[-1]:
                return False
            stack.pop()
        else:
            stack.append(char)
    if stack:
        return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
