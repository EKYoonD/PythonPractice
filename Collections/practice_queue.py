import queue
import heapq

# 파일명을 queue로 만들어버리면, 그 파일에서 import해와서 안됨!! 주의!!

# FIFO
import random

q = queue.Queue()

for i in range(3):
    q.put(i)

while not q.empty():
    print(q.get(), end=" ")

print()

# LIFO
lq = queue.LifoQueue()

for i in range(5):
    lq.put(i)

while not lq.empty():
    print(lq.get(), end=" ")
print()


# 우선순위큐
# 우선순위에 따라서 아이템을 정렬하고, 우선 순위가 가장 높은 아이템을 pop하는 queue
# 이게 첫번째 인자가 우선순위큐라기 보다는
# tuple 자체가 앞에 숫자를 비교하고 -> 같으면 다음 문자를 비교하고 하는 특성을 가지고 있기 때문
pq = queue.PriorityQueue()
for i in range(10):
    pq.put((random.randint(1,10), i))

while not pq.empty():
    # print(pq.get()[0], end=" ")
    print(pq.get()[1], end=" ")


class PriorityQueue:
    # list와 idx라는 기본 변수를 가지게 됨
    def __init__(self):
        self.list = []
        self.idx = 0

    def put(self, item, priority):
        heapq.heappush(self.list, (priority, self.idx, item))