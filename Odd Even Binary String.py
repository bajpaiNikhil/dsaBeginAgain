

t = int(input())
for t in range(t):
    n = int(input())
    l= list(map(int,input().split()))
    a = l.count(0)
    if a&1!=0:
        print("NO")
    else:
        print("YES")