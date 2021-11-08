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
    print('%s:%d' %(n, container[n]), end=" ")
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
