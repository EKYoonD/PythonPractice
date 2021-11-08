from bisect import bisect_left, bisect_right

a = [1, 2, 2, 4, 4, 4, 6]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
print()


def count_by_range(bisect_test_list, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    print(right_index)
    print(left_index)
    return right_index - left_index


bisect_test_list = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 8]

print(count_by_range(bisect_test_list, 4, 4))
print(count_by_range(bisect_test_list, -1, 3))

