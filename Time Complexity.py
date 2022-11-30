

t = int(input())
for t in range(t):
    m , n = map(int,input().split())
    if m == n:
        print("NO")
    elif m>n:
        print("YES")
    else:
        print("NO")