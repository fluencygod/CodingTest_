from itertools import product

N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]
for i in list(product(num_list, repeat=M)):
    print(*i)
