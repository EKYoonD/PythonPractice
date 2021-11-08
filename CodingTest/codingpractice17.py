n, m = map(int, input().split())
x, y, direction = map(int, input().split())
map_loc = [[0]*m for _ in range(n)]

# 현재 위치 초기화 (방문했음)
map_loc[x][y] = 1

# map 정보 세팅하기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))


# 동서남북별로 나눠 놓기
map_x = [-1, 0, 1, 0]
map_y = [0, 1, 0, -1]


# 왼쪽으로 회전 (map에서 움직이는 위치가 달라짐 -> map_x, map_y -1 씩 해서 맞는 방향 찾아줘
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    # print(direction)
    nx = x + map_x[direction]
    ny = y + map_y[direction]
    # 아직 방문 안했고(map_loc은 내가 방문했나, 안했나 -> 안했다 : 0) 육지다(array는 입력받은 바다, 육지 -> 육지 : 0)
    if map_loc[nx][ny] == 0 and array[nx][ny] == 0:
        map_loc[nx][ny] = 1
        print(nx, ny, map_loc[nx][ny])
        x = nx
        y = ny
        count += 1
        # 초기화
        turn_time = 0
        continue
    # 이미 간 곳이거나(1) 바다면(1) turn_time +1 하면서 다음 for값 들어가게
    else:
        turn_time += 1
    # 위 과정 다 끝난 결과,
    # 네 방향 다 돌았을 때(turn_time == 4) -> 더 이상 갈 데가 없을 때
    if turn_time == 4:
        # 일단 원상복귀
        nx = x - map_x[direction]
        ny = y - map_y[direction]
        # 뒤로 갈 수 있다면 뒤로 가기 (뒤가 육지라 0이다)
        if array[nx][ny] == 0:
            x = nx
            y = ny
            print(nx, ny, map_loc[nx][ny])
            count += 1
        else:
            break
        turn_time = 0

print(count)