


t = int(input())
for t in range(t):
    l = list(map(int,input().split()))
    l.sort()
    if l[-1]==(l[0]+l[1]):
        print("YES")
    else:
        print("NO")