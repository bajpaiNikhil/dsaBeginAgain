
t = int(input())
for t in range(t):
    n, m = map(int , input().split())
    l = list(map(int , input().split()))[:n]
    s = set(l)
    if len(s) <= abs(n - m):
        print(len(s))
    else:
        print(abs(n-m))

