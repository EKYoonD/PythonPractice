numbs = {0: 'zero', 1: 'one', 2: 'two', 3: 'three',
         4: 'four', 5: 'five', 6: 'six', 7: 'seven',
         8: 'eight', 9: 'nine', 10: 'ten'}


def solution(s):
    answer = ""
    for i in range(0, len(s)):
        if s[i].isnumeric():
            answer += numbs[int(s[i])]
        else:
            answer += s[i]
    return answer


print(solution("1zerotwozero3"))


