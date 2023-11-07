from itertools import permutations

N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]
for i in list(permutations(num_list, M)):
    print(*i)
