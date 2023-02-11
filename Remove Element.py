t = int(input())
for t in range(t):
    n,m = map(int,input().split())
    l = list(map(int,input().split()))
    lMax = max(l)
    lMin = min(l)

    if n ==1 or lMin+lMax <= m:
        print("YES")
    elif lMax>m or lMin+lMax >m:
        print("NO")