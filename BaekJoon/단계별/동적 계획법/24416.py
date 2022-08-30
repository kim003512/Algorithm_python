N = int(input())
fibNum, fiboNum = 0, 0
f = [0 for _ in range(41)]

def fib(n) :
    global fibNum
    if n == 1 or n == 2 :
        return 1
    else :
        fibNum += 1
        return fib(n-1) + fib(n-2)

def fibonacci(n) :
    global fiboNum
    f[1], f[2] = 1, 1
    for i in range(3, n+1) :
        fiboNum += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

fib(N)
fibonacci(N)

print(fibNum+1, fiboNum)