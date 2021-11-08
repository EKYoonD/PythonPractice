def solution(a, b):
    sum_ab = 0
    for i in range(len(a)):
        sum_ab += a[i] * b[i]
    return sum_ab


list1 = [-1, 0, 1]
list2 = [1, 0, -1]
print(solution(list1, list2))


def solution3(c, d):
    return sum(x * y for x, y in zip(c, d))


print(solution3(list1, list2))

list3 = list([(x, y) for x, y in zip(list1, list2)])

print(list3)