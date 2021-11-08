def division(number):
    cnt = 0
    for i in range(1, number + 1):
        if number % i == 0:
            cnt = cnt+1
    return cnt


def solution(left, right):
    sum_number = 0
    for num in range(left, right+1):
        if division(num) % 2 == 0:
            sum_number = sum_number + num
        if division(num) % 2 == 1:
            sum_number = sum_number - num
    return sum_number


print(solution(13, 17))
