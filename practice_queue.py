import queue

# 우선순위 queue = PriorityQueue (변형 구조)
data_que = queue.PriorityQueue()

data_que.put((10, "Korea"))
data_que.put((15, "USA"))
data_que.put((20, "China"))

print(data_que.qsize())

# 우선순위 높은 queue 부터 get
print(data_que.get())
print(data_que.qsize())

# queue를 list()로 구현해보기
queue_list = list()

# 새로운 요소 넣는 것 = enqueue, 요소 제거하는 것 = dequeue (FIFO가 기본)
def enqueue(data):
    queue_list.append(data)


# 사실 pop()해도 됨
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data


for index in range(10):
    enqueue(index)

print(queue_list)
print(dequeue())
print(queue_list)
