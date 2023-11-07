from itertools import combinations_with_replacement

N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]
for i in list(combinations_with_replacement(num_list, M)):
    print(*i)
