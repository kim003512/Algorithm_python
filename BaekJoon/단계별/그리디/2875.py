n, m, k = map(int, input().split())

team = 0
while True :
    n -= 2
    m -= 1

    if n<0 or m<0 or (n+m)<k :
        break
    team += 1
print(team)

""" for i in range(k) :
    if n // 2 > m :
        n -= 1
    else :
        m -= 1

print(min(n//2, m)) """
"""
team = 0

if n > m :
    n -= k
else :
    m -= k

while n != 0 or m != 0:
    n -= 2
    m -= 1
    team += 1

print(team)


 if n < 2 or m <1 :
    break """