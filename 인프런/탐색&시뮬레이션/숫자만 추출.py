string = input()
strList = list(string)

for i in strList :
    if type(i) != type(0) :
        strList.remove(i)
print(strList)
'''
for i in range(len(strList)) :
    print(strList[i])
    if type(strList[i]) != type(0) :
        strList.remove(strList[i])

print(strList)
'''