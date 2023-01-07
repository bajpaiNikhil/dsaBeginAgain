



t = int(input())
for t in range(t):
    a,b,c = map(int,input().split())
    k = a^b^c
    if (a^k+b^k)!=c^k:
        print("NO")
    else:
        print("YES")