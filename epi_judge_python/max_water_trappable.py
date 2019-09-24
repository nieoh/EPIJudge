from test_framework import generic_test


def calculate_trapping_water(heights):
    total_water = 0
    n = len(heights)
    fmax = 0
    forward_max = [0] * n
    bmax = 0
    backward_max = [0] * n

    for i in range(n):
        fmax = max(fmax, heights[i])
        forward_max[i] = fmax
        bmax = max(bmax, heights[n-1-i])
        backward_max[n-1-i] = bmax

    for i in range(n):
        h = min(forward_max[i], backward_max[i])
        total_water += (h-heights[i])


    return total_water


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_water_trappable.py",
                                       'max_water_trappable.tsv',
                                       calculate_trapping_water))
