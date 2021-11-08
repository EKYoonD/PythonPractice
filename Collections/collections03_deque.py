import collections

# deque : 양방향 큐 (컨테이너 앞뒤에 넣거나 뺄 수 있다)

deq = collections.deque("Hello Python")
deq1 = collections.deque('Nice to meet you')
deq2 = collections.deque({
    1: 'Hi',
    2: 'My name is Katie',
    3: 23
})

print(deq, 1)

deq = collections.deque(list(deq))
print(deq)

deq.reverse()
print(deq)
deq3 = collections.deque(["aaa", 'BBB', 'ccc'])
print(deq3.popleft())


deq2.append('가')

list1 = ["hihihimynameiskatie", 'hihihi']
sorted(list1)
print(list1)
list1.reverse()
print(list1)
while len(deq2) > 0:
    print(deq2.pop())

print(deq)
print(len(deq))
print(deq[0])
print(deq[-1])


deq1 = sorted(deq1)

sample = ""
for i in deq1 :
    sample += i

print(sample)

print(deq1, 123)
deq.remove('o')
deq.remove('H')
deq.reverse()
print(deq)
#
# deq.append("k")
# print(deq)
# deq.appendleft("k")
# print(deq)
#
# deq.extendleft('d')
# print(deq)
#
# deq.extend('e')
# print(deq)
#
# deq1 = collections.deque()
# deq1.extend("가나다라마바사")
# deq1.extendleft("오")
# print(deq1)

# 오른쪽에서 꺼내오기
# 한번만 꺼낼 수 있음
# while True:
#     try:
#         print(deq.pop()),
#     except IndexError:
#         break

while True:
    try:
        print(deq.popleft(), end = ''),
    except IndexError:
        break

print()

#
# while True:
#     try:
#         print(deq.pop(), end = "    ")
#     except IndexError:
#         break

test = [1, 2, 3]
print(test.__dir__())
print(dir(test))

teststr = "123abc"
print(dir(teststr))
print(enumerate(teststr))
for i, j in enumerate(teststr):
    print(i, j)

print(eval("12+33"))