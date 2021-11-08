board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    list_get = list()
    cnt = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] - 1] != 0:
                list_get.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break

            if len(list_get) > 1:
                if list_get[-1] == list_get[-2]:
                    list_get.pop()
                    list_get.pop()
                    cnt += 2
    return cnt

print(solution(board, moves))