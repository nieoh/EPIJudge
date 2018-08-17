from test_framework import generic_test


def flip_color(x, y, image):
    color = image[x][y]
    def flip(curr):
        a, b = curr
        if not(0 <= a < len(image) and 0 <= b < len(image[a])) or image[a][b] != color:
            return
        image[a][b] = color^1
        candidates = [(a-1, b), (a+1, b), (a, b-1), (a, b+1)]
        for cand in candidates:
            flip(cand)
        return

    flip((x, y))
    return 


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
