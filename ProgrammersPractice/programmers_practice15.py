def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == False:
            signs[i] = -1
        if signs[i] == True:
            signs[i] = 1
    return sum(x*y for x, y in zip(absolutes, signs))

print(solution([4,7,12], [True,False,True]))