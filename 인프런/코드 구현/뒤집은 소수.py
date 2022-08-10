n = int(input())
#numList = list(int(input().split()) for _ in range(n))
numList= list(map(int, input().split()))

def reverse(x) :
    res = 0
    while x > 0 :
        t = x % 10
        res = res * 10 + t
        x = x //10
    return res
#    return int(str(x)[::-1])

def isPrime(x) :
    if x == 1 :
        return False
    for i in range(2, x) : # why x? x+1?
        if x % i == 0 :
            return False
    return True

for i in range(len(numList)) :
    if(isPrime(reverse(numList[i]))) :
        print(reverse(numList[i]), end=' ')