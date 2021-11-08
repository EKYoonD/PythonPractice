def solution(n):
    answer = ''
    reminder = 0

    while n > 0:
        reminder = n % 3
        n = n//3

        if reminder == 0:
            n -= 1
            reminder = 4

        answer = str(reminder) + answer

    return answer

print(solution(24))