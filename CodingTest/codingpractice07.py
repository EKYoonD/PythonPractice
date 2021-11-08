number, N = map(int, input().split())
count = 0

while True:
    if number % N == 0 :
        number /= N
        count += 1
    else:
        number -= 1
        count += 1
    if number == 1:
        break

print(number, count)