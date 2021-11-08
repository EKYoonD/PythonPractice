from pprint import pprint
import array

# pprint(pretty print) : 자료 구조를 사람이 보기 좋게 출력하는 모듈

# tuple 안 dictionary
data = [(1, {"a": "가", "b": "나", "c": "다"}),
        (2, {"e": "마", "f": "바", "g": "사"}),
        (3, {"h": "아"})]

pprint(data)

# array : 같은 자료형 -> 메모리 낭비 줄일 수 있음

str = "abcdefg"

arr = array.array("u", str)  # array(타입 코드를 넣어줘야함, 데이터) -
print(arr)

arr1 = array.array('i', range(-5, 5))
print(arr1)
arr1.extend(range(5))
print(arr1[3:6])

arrlist = list(enumerate(arr1))
print(arrlist)

for i,j in enumerate(arr1):
        print(i, ":", j, end=" ")