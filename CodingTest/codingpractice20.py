# BFS
from collections import deque


def bfs(tree_graph, start, visited_tf):
    # queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    visited[start] = True
    # queue가 빌때까지 반복
    while queue:
        # queue에서 원소 하나 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")
        # 해당 원소와 연결된, 아직 방문하지 않은 모든 원소들을 queue에 삽입
        for i in tree_graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
