def sumNumber(number):
    sum = 0
    for i in range(number+1):
        sum = sum + i
    return sum


def sumNumberAll(number):
    return int(number * (number + 1) / 2)


print(sumNumber(100))
print(sumNumberAll(100))