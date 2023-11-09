import sys
from collections import deque
sys.setrecursionlimit(150000)


def bfs(r):
    global cnt
    visited[r] = cnt
    queue = deque([r])
    while queue:
        u = queue.popleft()
        graph[u].sort()
        for g in graph[u]:
            if visited[g] == 0:
                cnt += 1
                visited[g] = cnt
                queue.append(g)

N, M, R = map(int, input().split())
visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
cnt = 1
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(R)
for i in range(1,N+1):
    print(visited[i])