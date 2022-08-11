'''a, b = map(int, input().split())

aArray, bArray = [], []
for i in range(1, a+1) :
    if a % i ==  0 :
        aArray.append(i)

for i in range(1, b+1) :
    if b % i == 0 :
        bArray.append(i)

print(max(set(aArray) & set(bArray)))
'''
import sys

A, B = map(int, sys.stdin.readline().split())

def gcb(a, b) :
    while b > 0 :
        a, b = b, a % b
    return a

def lcm(a, b) :
    return int(a* b / gcb(a, b))

print(gcb(A, B))
print(lcm(A, B))