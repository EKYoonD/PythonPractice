def solution(lotto_num, win_nums):
    cnt = 0
    max_cnt = 0
    for i in lotto_num:
        if i == 0:
            max_cnt += 1
        for j in win_nums:
            if i == j:
                cnt += 1
                max_cnt += 1

    if cnt == 0:
        cnt = 1
    if max_cnt == 0:
        max_cnt = 1

    answer = [7-max_cnt, 7-cnt]
    return answer


lot_num = [0, 0, 0, 0, 0, 0]
win_num = [20, 9, 3, 45, 4, 35]

print(solution(lot_num, win_num))
