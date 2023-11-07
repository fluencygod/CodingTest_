def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n, cnt):
    f = [0 for _ in range(n)]
    f[0] = 1
    f[1] = 1
    for i in range(2,n):
        cnt = cnt+1
        f[i] = f[i-1] + f[i-2]
    return cnt


if __name__ == '__main__':
    n = int(input())
    print(fib(n), fibonacci(n, 0))
