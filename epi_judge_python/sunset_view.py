from test_framework import generic_test


def examine_buildings_with_sunset(sequence):
    # TODO - you fill in here.
    if not sequence:
        return []
    ret = [(sequence[-1], len(sequence)-1)]
    for i, h in enumerate(reversed(sequence[:-1])):
        if h > ret[-1][0]:
            ret.append((h, len(sequence)-i-2))
    return [r[1] for r in ret]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
