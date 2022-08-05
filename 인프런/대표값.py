N = int(input())

gradeList = list(map(int, input().split()))

sum=0
for i in range(N) :
    sum += gradeList[i]
    i += 1
    
sum = round(sum//N, 1)

print(sum) 