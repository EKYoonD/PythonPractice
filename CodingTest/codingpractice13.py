import heapq

data = [i for i in range(10)]


# 기본적으로 pythond의 heapd은 minheap 제공 (이진트리에서 가장 위가 가장 작은 -> 0부터 대입했을때 자연히 0, 1, 2.. 저장된다
# 하지만 maxheap은 아니다 (0, -1, -2 이런식으로 저장해봤을때 이진트리 위를 밀면서 들어감 자식이 차있으면 다음 거에 들어가서 채워준다)

def heapsort(iterable_data):
    h = []
    result1 = []

    for value in iterable_data:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result1.append(heapq.heappop(h))
    return result1


result = heapsort(data)
print(result)


def max_heap(iterable_data):
    h = []
    result2 = []

    for value in iterable_data:
        # -로 넣으면 일단 부호만 빼면 maxheap처럼 보임
        heapq.heappush(h, -value)
        # 보면서 확인해
        print(h)
    for i in range(len(h)):
        # 사실상 제일 작은거 꺼낸건데 그거에서 -붙여서 제일 큰 값 붙인 것처럼 보여주는 것
        result2.append(-heapq.heappop(h))
        print(result2)
    return result2


print(max_heap(data))
