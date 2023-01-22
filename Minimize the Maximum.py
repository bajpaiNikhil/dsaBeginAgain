import math

t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    ans = l[0]
    sum = l[0]
    for i in range(1,len(l)):
        sum += l[i]
        ans = max(ans, math.ceil(sum/ (i + 1)))
    print(ans)
