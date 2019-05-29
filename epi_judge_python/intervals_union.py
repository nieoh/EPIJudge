import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

#Interval = collections.namedtuple('Interval', ('left', 'right'))

class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.left.val != other.left.val:
            return self.left.val < other.left.val
        return self.left.is_closed and not other.left.is_closed

        
def union_of_intervals(intervals):
    intervals.sort()
    ret = [intervals[0]]
    for interval in intervals:
        if (interval.left.val > ret[-1].right.val) or (interval.left.val == ret[-1].right.val and not interval.left.is_closed and not ret[-1].right.is_closed):
            ret.append(interval)
        elif interval.right.val > ret[-1].right.val:
            ret[-1].right = interval.right
        elif interval.right.val == ret[-1].right.val:
            ret[-1].right = Endpoint((ret[-1].right.is_closed or interval.right.is_closed), ret[-1].right.val)
    return ret


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
