

t = int(input())
for t in range(t):
    n ,m = map(int , input().split())
    l = list(map(int,input().split()))
    l.sort()
    if n>m:
        print(l[m])
    else:
        print(max(l))
