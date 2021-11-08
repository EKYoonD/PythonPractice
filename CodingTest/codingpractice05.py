k = int(input())

changes = [500, 100, 50, 10]
change_num = 0


for change in changes:
    while change <= k:
        k -= change
        change_num += 1
        print(k, change, change_num)
        if k == 0:
            break
    if k == 0:
        break
print(change_num)