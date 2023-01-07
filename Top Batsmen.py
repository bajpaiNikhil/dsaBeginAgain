#

t = int(input())
for t in range(t):
    l = list(map(int,input().split()))
    n = int(input())
    l.sort()
    k = sum(l[len(l)-n:])
    print(l, n,k)




