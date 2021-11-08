def solution(sco_list, K):
    cnt = 0

    def pattern(sc_list):
        sc_list.sort()
        sc_min = sc_list[0] + (sc_list[1] * 2)
        del sc_list[0]
        sc_list[1] = sc_min

    def compare(nums, K):
        for num in nums:
            if num < K:
                return False
        return True

    while True:
        pattern(sco_list)
        if compare(sco_list, K):
            break
        else:
            cnt += 1
    return cnt


print(solution([1, 2, 3, 9, 10, 12], 7))

