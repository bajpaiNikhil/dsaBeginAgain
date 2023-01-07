import math

t = int(input())
for t in range(t):
    n = int(input())
    maximumIs = []
    for i in range(n):
        s,p,v = map(int,input().split())
        k = v*math.floor(p/(s+1))
        maximumIs.append(k)
    print(max(maximumIs))
