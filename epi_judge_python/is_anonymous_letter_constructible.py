from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    if len(letter_text) > len(magazine_text):
        return False
    dic = {}
    for ch in letter_text:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1

    for ch in magazine_text:
        if ch in dic:
            dic[ch] -= 1
            if dic[ch] == 0:
                del dic[ch]
                if not dic:
                    return True

    return not dic

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
