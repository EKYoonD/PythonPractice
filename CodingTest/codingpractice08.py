size = int(input())
moves = list(input().split())

LR = 1
UD = 1

for move in moves:
    if move == 'R':
        if LR == 5:
            LR = 5
        LR += 1

    if move == 'L':
        if LR == 1:
            LR = 1
        LR -= 1

    if move == 'D':
        if UD == 5:
            UD = 5
        UD += 1

    if move == 'L':
        if UD == 1:
            UD = 1
        UD -= 1

print(UD, LR)