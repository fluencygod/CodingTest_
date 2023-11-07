from itertools import combinations

N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]
for i in list(combinations(num_list, M)):
    print(*i)
