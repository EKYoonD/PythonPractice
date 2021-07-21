num_list = [0, -11, 31, 22, -11, 33, -44, -55]
right_num = list()

for index, num in enumerate(num_list):
    if num > 0:
        right_num.append(num)

print(right_num)