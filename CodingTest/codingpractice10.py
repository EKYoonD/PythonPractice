# ord('a') = 97
# ord('h') = 104

current = list(input())
first = ord(current[0])
second = int(current[1])
count_ways = 0

ways = [2, 1, -2, -1]

for way_first in ways:
    if (first + way_first >= 97) and (first + way_first <= 104):
        if abs(way_first) == 1 :
            ways = [2, -2]
        if abs(way_first) == 2 :
            ways = [1, -1]
        for way_second in ways:
            if (second + way_second >= 1) and (second + way_second <= 8):
                print(first+way_first, second+way_second)
                count_ways += 1

print(count_ways)

