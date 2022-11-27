from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    