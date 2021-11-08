from collections import deque

n, m = map(int, input().split())

map_graph = []
map_x = [-1, 1, 0, 0]
map_y = [0, 0, -1, 1]

for i in range(n):
    map_graph.append(list(map(int, input().split())))

print(map_graph)
print("--------------------------------")


def map_maze(index_x, index_y):
    maze_queue = deque()
    maze_queue.append((index_x, index_y))
    print(maze_queue)
    while maze_queue:
        index_x, index_y = maze_queue.popleft()
        print("================================")
        print(index_x, index_y)
        print("================================")
        for point in range(4):
            nx = index_x + map_x[point]
            ny = index_y + map_y[point]
            print(nx, ny)
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                print("pass")
                continue
            if map_graph[nx][ny] == 0:
                print("wall")
                continue
            if map_graph[nx][ny] == 1:
                print("found -> ")
                map_graph[nx][ny] = map_graph[index_x][index_y] + 1
                maze_queue.append((nx, ny))
            else:
                print("already visited")
                continue
            print("--------------------------------")
            print(map_graph)
            print(maze_queue)
            print("--------------------------------")
    return map_graph[n-1][m-1]


print("answer : ", map_maze(0, 0))



