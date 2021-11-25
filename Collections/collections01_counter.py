import collections

print(collections.Counter(['aa', 'cc', 'dd', 'aa', 'bb', 'ee']))
print(collections.Counter({'가': 3, "나": 2, "다": 4}))
print(collections.Counter(a=2, b=4, c=1))

firstCount = collections.Counter(['aa', 'cc', 'dd', 'aa', 'bb', 'ee', 1])
print(firstCount)

# Counter로 이루어진 container 생성 가능
# collections.Counter()는 항상 dictionary 형태로 return
container = collections.Counter()
print(container)

container.update("aabbcsscccff")
print(container)

container.update("cccccccccccccc")
print(container)

for n in "abccdfe":
    print('%s:%d' % (n, container[n]), end=" ")
print()

ct = collections.Counter("Hello")
ct['x'] = 0
print(ct)
print(list(ct.elements()))

str_strip = '0000000Water boils at 100 degrees 000'
str_strip = str_strip.strip("0")
print(str_strip)

# most common(n) 객체 사용하기 : 상위 n 개의 sequence 만듬 (파일 지금 없음)
# rt : text mode, f란 이름으로
ct2 = collections.Counter()
# with open('test.txt', 'rt') as f:
#     for li in f:
#         ct2.update(li.lstrip().lower())
#         li = li.lstrip("*")
#         print(li)

# print(ct2)
#
# for item, cnt in ct2.most_common(5):
#     print('%s : %2d' %(item, cnt))
#
# print(ct2.most_common())

# Counter는 산술/집합 연산이 가능

ct3 = collections.Counter(['a', 'b', 'c', 'd', 'd', 'd', 'e'])
ct4 = collections.Counter('aeroplane')

print(ct4.values())
print((ct3 - ct4))
print((ct3 & ct4))

list_test = [i for i in range(10)]
list_test.pop(8)
print(list_test)

print(8 in list_test)

print(sorted('Python'))

tuple_test = (2, 3, 4)
print(tuple_test)

test = [1, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5]
set_test = set(test)
print(set_test)
set_test.add(19)
set_test.remove(3)
print(set_test)

sample_dict = {1: 'katie', 2: 'changho', 3: 'zichang'}
print(sample_dict.get(1, 0))
print(sample_dict.get(4, 0))
print(sample_dict.keys())

check_list = [3, 4, 5, 6]

for i in sample_dict:
    print(i in check_list)

del (sample_dict[1])
print(sample_dict)

print(3 in sample_dict)

result = 0 or 100  # 참인데... or 의 결과가 True 가 아니다?  int 100 이다?
print(result)
result = "Hello" or "Python"  # "Hello"
print(result)
result = "Hello" and "Python"  # "Python"
print(result)
result = [] and "Python"  # []
print(result)
result = {'name': 'yoon'} or (1, 2, 3)
print(result)

a, b = divmod(13, 3)
print(a)

print(list_test)
for i, j in enumerate(list_test):
    print(i, j)

print(pow(2, 5))

from functools import reduce


def add(x, y):
    print((x, y))
    return x + y


print(reduce(lambda x, y: x + y, [1, 3, 5, 7, 9]))


def func(x, y):
    x.append(y ** 2)
    return x


print(reduce(func, [1, 4, 9], []))
