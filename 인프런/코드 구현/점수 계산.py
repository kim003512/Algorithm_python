n=int(input())
a=list(map(int, input().split()))
cnt=0
sum=0
for i in range(n):
    print(a[i])
    if a[i]==1:
        cnt=cnt+1
        sum=sum+cnt
        print(cnt, sum)
    else:
        cnt=0

print(sum)

'''
n = int(input())
grade = list(map(int, input().split()))

sum = 0
for i in range(n) :
    if i == 0 :
        if grade[i] == 1 :
            sum += 1
    elif i == 1 :
        if grade[i-1] == 1 :
            sum += 2
        else :
            sum += 1
    else :
        if grade[i-2] == 1 and grade[i-1] == 1 and grade[i] == 1:
            sum +=3
        elif grade[i-2] == 0 and grade[i-1] == 1 and grade[i] == 1:
            sum +=2
        elif grade[i] == 1 :
            sum += 1

print(sum)
'''

    