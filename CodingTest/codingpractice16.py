import math

def prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            # print("not a prime number")
            # 잘 구분해야 할 것 : return 은 아예 끝나는 거 def -> return, for -> break/continue
            return False
        # if i == number-1:
        #     print("prime number")
        #     return True
    return True


def prime_number_sqrt(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


print(prime_number(21))
print(prime_number(23))

print(prime_number_sqrt(21))
print(prime_number_sqrt(23))