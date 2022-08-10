import sys

n = int(sys.stdin.readline())

stringArray = [sys.stdin.readline().strip() for _ in range(n)]

for i in range(len(stringArray)) :
    stringArray[i] = stringArray[i].lower()
    if stringArray[i] == stringArray[i][::-1] :
        print("#%d %s" %(i+1, 'YES'))
    else :
        print("#%d %s" %(i+1, 'NO'))