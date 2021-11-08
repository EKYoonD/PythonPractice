# bisect 모듈
# 정렬된 상태를 만들면서 원소를 추가함 (Heap은 list를 생성한 다음 정렬)
# list의 길이가 상당히 긴 경우 Bisect는 Heap에 비해 정렬 속도가 빠름

import random
import bisect

list_sample = []
for i in range(1, 15):
    num = random.randint(1,100)
    # 첫번째 매개변수는 값을 추가할 iterable(list),
    # 두번째 매개변수는 추가할 값
    # bisect.bisect는 num 이 정렬된 list_sample에 들어갔을 때 어느 위치에 들어갈 수 있는지
    pos = bisect.bisect(list_sample, num)
    # 리스트를 정렬 상태로 유지시킨 채로 정렬될 수 있는 위치에 해당 항목을 삽입한다.
    bisect.insort(list_sample, num)
    print('%3d %3d'%(num, pos), list_sample)

list_sample_2 = [i for i in range(-5, 10, 2)]


def counts_in_range(start, end, sample_list):
    start = bisect.bisect_left(sample_list, start)
    end = bisect.bisect_right(sample_list, end)
    return end-start


print(list_sample_2)
print(counts_in_range(0, 9, list_sample_2))
