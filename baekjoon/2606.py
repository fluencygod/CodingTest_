def dfs(r):
    visited[r] = 1
    for g in graph[r]:
        if visited[g] == 0:
            dfs(g)

import sys
sys.setrecursionlimit(150000)

N = int(input())
M = int(input())
visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)
print(sum(visited)-1)