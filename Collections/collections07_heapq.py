import heapq
from showHeap import show_tree
from heapData import data

print(data)


def push_min_heap(data):
    heap1 = []
    for i in data:
        heapq.heappush(heap1, i)
    return heap1


def pop_min_heap(data):
    heapq.heapify(data)
    while True:
        if len(data) == 0:
            break
        else:
            print(heapq.heappop(data), end=" ")


def push_max_heap(data):
    heap1 = []
    data = list(map(lambda x : x*(-1), data))
    for i in data:
        heapq.heappush(heap1, -i)
    return heap1


def pop_max_heap(data):
    data = list(map(lambda x: x * (-1), data))
    heapq.heapify(data)
    while data:
        print(-heapq.heappop(data), end=" ")


# def pop_max_heap(data):
#     data = list(map(lambda x: x * (-1), data))
#     heapq.heapify(data)
#     while data:
#         if len(data) == 0:
#             break
#         else:
#             print(-heapq.heappop(data), end=" ")


print(push_max_heap(data))
print(pop_max_heap(data))
print(push_min_heap(data))

a = heapq.nlargest(len(data), data)

heapq.heapreplace(data, 16)
print(data)

for i in range(len(a)) :
    print(i+1, '번째 큰 수는 ', a[i], '이다')

heapq.heapreplace(data, 1)
print(data, "!!")
print(data[0])

print(a)
print(sum(a))
print(heapq.nsmallest(3, data))

print(pop_min_heap(data))


data = [10, 3, 2, 9, 8, 6, 3]
heap = []


new = []
heapq.heapify(new)

heapq.heappush(new, (3, 'enjoy'))
heapq.heappush(new, (9, 'wow'))
heapq.heappush(new, (6, '???'))

while True:
    if len(new)== 0:
        break
    else:
        print(heapq.heappop(new))

print(new)

for num in data:
    heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
    print(heapq.heappop(heap)[1], end=" ")  # index 1