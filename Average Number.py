t = int(input())
for t in range(t):
    a, b, c = map(int, input().split())
    l = list(map(int, input().split()))
    k = sum(l)
    z = (a+b)*c - k

    if z%b == 0 and z/b> 0:
        print((z//b) )
    else:
        print(-1)




