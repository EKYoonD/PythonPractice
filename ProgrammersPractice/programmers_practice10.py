def solution(numbers, hand):
    answer_number = ""
    first_right = [3, 2]
    first_left = [3, 0]

    hand_range = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                  4: [1, 0], 5: [1, 1], 6: [1, 2],
                  7: [2, 0], 8: [2, 1], 9: [2, 2],
                  0: [3, 1]}

    for number in numbers:
        if number in (3, 6, 9):
            answer_number += "R"
            first_right = hand_range[number]
        elif number in (1, 4, 7):
            answer_number += "L"
            first_left = hand_range[number]
        else:
            if abs(hand_range[number][0]-first_right[0]) + abs(hand_range[number][1]-first_right[1]) > abs(hand_range[number][0]-first_left[0]) + abs(hand_range[number][1]-first_left[1]):
                answer_number += "L"
                first_left = hand_range[number]
            elif abs(hand_range[number][0]-first_right[0]) + abs(hand_range[number][1]-first_right[1]) < abs(hand_range[number][0]-first_left[0]) + abs(hand_range[number][1]-first_left[1]):
                answer_number += "R"
                first_right = hand_range[number]
            else:
                if hand == "right":
                    answer_number += "R"
                    first_right = hand_range[number]
                elif hand == "left":
                    answer_number += "L"
                    first_left = hand_range[number]
    return answer_number


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
