given_answer1 = "1 2 3 4 5 6 7 8"
given_answer2 = "8 7 6 5 4 3 2 1"
given_answer3 = "3 6 4 5 1 7 8 2"


def solution(s):
    split_s = s.split(" ")
    check = 0
    if split_s[0] == "8":
        for i in range(len(split_s) - 1):
            if split_s[i] > split_s[i + 1]:
                check = 1
            else:
                check = 0
                break

    if split_s[0] == "1":
        for i in range(len(split_s) - 1):
            if split_s[i] < split_s[i + 1]:
                check = -1
            else:
                check = 0
                break

    if check == 1:
        print("descending")
    elif check == -1:
        print("ascending")
    else:
        print("mixed")


solution(given_answer3)
solution(given_answer1)
solution(given_answer2)
