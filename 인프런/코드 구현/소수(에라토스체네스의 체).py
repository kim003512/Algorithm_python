import math

n = int(input())
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1) : #2~n의 제곱근까지 모든 수 확인
    if array[i] == True : 
        j = 2
        while i * j <= n :
            array[i*j] = False
            j += 1

for i in range(2, n+1) :
    if array[i] :
        print(i, end=' ')


'''
def primeNum(num) :
    for i in range(2, num) :
        if num % i :
            return False
    print()
'''

