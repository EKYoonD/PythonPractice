def solution(s):
    numbs = {'zero': 0, 'one': 1, 'two': 2, 'three': 3,
             'four': 4, 'five': 5, 'six': 6, 'seven': 7,
             'eight': 8, 'nine': 9}

    dict_num = {0: 'zero', 1: 'one', 2: 'two', 3: 'three',
                4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                8: 'eight', 9: 'nine'}

    for j in range(0, 10):
        if s.find(dict_num[j]) is not None:
            s = s.replace(dict_num[j], str(numbs[dict_num[j]]))
    return int(s)


# 더 멋있는 정답
# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
#
# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)


print(solution("1zerotwozero3"))