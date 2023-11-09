def dfs(r):
    global cnt
    visited[r] = cnt
    graph[r].sort()
    for g in graph[r]:
        if visited[g] == 0:
            cnt += 1
            dfs(g)

import sys
sys.setrecursionlimit(150000)

N, M, R = map(int, input().split())
visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
cnt = 1
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(R)
for i in range(1,N+1):
    print(visited[i])