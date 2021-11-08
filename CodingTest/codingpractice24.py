array1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택정렬 (selection sort)
for i in range(len(array1)):
    min_index = i
    for i in range(i+1, len(array1)):
        if array1[min_index] >= array1[i]:
            temp = array1[min_index]
            array1[min_index] = array1[i]
            array1[i] = temp

print(array1)

# python에서 swap
array2 = [3, 5]
array2[0], array2[1] = array2[1], array2[0]
print(array2)


array3 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


# 삽입정렬 (insertion sort)
