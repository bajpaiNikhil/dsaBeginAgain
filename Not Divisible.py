
#do remember 1....n-1 are not divisible by n
t = int(input())
for t in range(t):
    n = int(input())
    l = []
    a = ""
    for i in range(n):
        if i&1 == 0:
            l.append(1)
            a += "1"
        else:
            l.append(0)
            a+="0"
    print(" ".join(a))