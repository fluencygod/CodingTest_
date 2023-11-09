from collections import deque

def bfs(graph, n, m):
    queue = deque()
    queue.append((0, 0))
    graph[0][0] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    return graph[m-1][n-1]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

M, N = map(int, input().split())
graph = []
for i in range(M):
    graph.append(list(map(int, input())))

answer = bfs(graph, N, M)
print(answer+1)