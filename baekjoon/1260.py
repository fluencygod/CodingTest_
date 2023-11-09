import sys
from collections import deque
sys.setrecursionlimit(150000)

def dfs(r):
    visited_1[r] = 1
    answer1.append(r)
    graph1[r].sort()
    for g in graph1[r]:
        if visited_1[g] == 0:
            dfs(g)
def bfs(r):
    visited_2[r] = 1
    answer2.append(r)
    queue = deque([r])
    while queue:
        u = queue.popleft()
        graph2[u].sort()
        for g in graph2[u]:
            if visited_2[g] == 0:
                visited_2[g] = 1
                answer2.append(g)
                queue.append(g)


N, M, R = map(int, input().split())
visited_1 = [0 for _ in range(N+1)]
visited_2 = [0 for _ in range(N+1)]
graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
answer1 = []
answer2 = []
for i in range(M):
    u, v = map(int, input().split())
    graph1[u].append(v)
    graph1[v].append(u)
    graph2[u].append(v)
    graph2[v].append(u)

dfs(R)
bfs(R)

print(*answer1)
print(*answer2)