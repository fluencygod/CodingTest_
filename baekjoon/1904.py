import sys
input = sys.stdin.readline
N = int(input())

x = [0] * (N+1)
x[1] = 1
if N>1:
    x[2] = 2
for i in range(3, N+1):
    x[i] = (x[i-1] + x[i-2]) % 15746
print(x[N])