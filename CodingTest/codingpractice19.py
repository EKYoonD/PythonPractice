# DFS
# graph:전체 그래프, v:시작 노드, visited:방문했는지 안했는지 True/False
def dfs(tree_graph, v, visited_tf):
    # 현재 노드 일단 방문 처리(v자리)
    visited_tf[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in tree_graph[v]:
        # print(tree_graph[v], i)
        # visited[v] == False
        if not visited_tf[i]:
            dfs(tree_graph, i, visited_tf)


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

dfs(graph, 1, visited)
