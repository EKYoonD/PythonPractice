def solution(brown, yellow):
    volume = brown + yellow
    xy = [0, 0]

    for x in range(1, volume):
        if volume % x == 0 and x <= int(volume / x) and (x-2)*(volume/x-2)==yellow:
            xy[0] = int(volume / x)
            xy[1] = x
    return xy


print(solution(10, 2))
print(solution(24, 24))
print(solution(8, 1))
