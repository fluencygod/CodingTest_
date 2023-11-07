T = int(input())
p = [0] * 101
p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10] = 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
for i in range(11, 101):
    p[i] = p[i-1] + p[i-5]
for _ in range(T):
    N = int(input())
    print(p[N])
