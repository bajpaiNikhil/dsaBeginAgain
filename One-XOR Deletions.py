t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    #print(d)
    ans = n - 1
    for i in range(n):
        #print(i , d[l[i]] , d[l[i^1]])
        ans = min(ans, n - d[l[i]] - d[l[i ^ 1]])
        #print(ans)
    print(ans)
