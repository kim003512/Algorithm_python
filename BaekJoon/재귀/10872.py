num = int(input())

def factory(n) :
    if(n == 0) :
        return 1
    else :
        return n * factory(n-1)

print(factory(num))