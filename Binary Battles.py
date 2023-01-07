

t = int(input())
for t in range(t):
    a , b , c = map(int,input().split())
    count=0
    while a > 0:
        if a & 1 != 1:
            count+=1
        a = a>>1
    print((count-1)*(b+c) + b)
