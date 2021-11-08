n, m = map(int, input().split())
ice_tray_map = []
result = 0

for row in range(n):
    ice_tray_map.append(list(map(int, input().split())))


def find_ice(x_index, y_index):
    if x_index <= -1 or x_index >= n or y_index <= -1 or y_index >= m:
        return False
    if ice_tray_map[x_index][y_index] == 0:
        ice_tray_map[x_index][y_index] = 1
        # 연결된 ice_tray가 있는지 DFS (연결이다? -> DFS
        # 연결된 ice_tray에 +1 / True 하는 게 아니라 방문했으면 1로 바꿔주는 역할!
        # 1로 바뀌고 다 죽음
        # 그래야 뒤에서 찾을때 1이라 넘어가게 (결국 root만 True, result+1되게 되어 있음)
        find_ice(x_index-1, y_index)
        find_ice(x_index, y_index-1)
        find_ice(x_index+1, y_index)
        find_ice(x_index, y_index+1)
        return True
    return False


for x_index in range(n):
    for y_index in range(m):
        # 원래 find_ice(x_index, y_index) == True
        if find_ice(x_index, y_index):
            result += 1


print("number of icetray :", result)