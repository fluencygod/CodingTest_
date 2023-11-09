from collections import deque

def bfs(graph, a, b, n, m):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j]==1:
                bfs(graph, i, j, N, M)
                cnt += 1
    print(cnt)