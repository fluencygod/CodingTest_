n = int(input())
x = list(map(int, input().split()))

for i in range(1, n):
    x[i] = max(x[i], x[i-1]+x[i])
print(max(x))