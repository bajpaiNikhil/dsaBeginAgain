

t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    k = []
    maxI = l[0]
    minI = l[0]
    flag = True
    for i in range(len(l)):
        maxI = max(maxI,l[i])
        minI = min(minI,l[i])
        if l[i]!=maxI and l[i]!= minI:
            flag = False
            break
    print("YES" if flag==True else "NO")