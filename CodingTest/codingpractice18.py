from collections import deque

queue = deque()
queue.append(3)
queue.append(5)
queue.append(8)
queue.append(4)
queue.pop()

queue.appendleft(10)
queue.appendleft(11)
queue.appendleft(12)
queue.appendleft(14)

print(queue)

queue.reverse()
print(queue)


def recursive_function(i):
    if i == 100:
        return
    recursive_function(i + 1)
    print(i+1, "번째 함수를 종료합니다")


def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n*factorial_recursive(n-1)


recursive_function(1)
print(factorial_iterative(5))
print(factorial_recursive(5))