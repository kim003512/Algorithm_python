def gdb(a, b) :
    if a % b == 0 :
        return b
    else :
        return gdb(b, a % b)

print(gdb(192, 162))