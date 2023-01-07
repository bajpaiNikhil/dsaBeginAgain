t = int(input())
for t in range(t):
    n, x, k = map(int, input().split())
    l = list(map(int, input().split()))[:n]
    m = list(map(int, input().split()))
    flag = True
    count = 0
    for i, j in zip(l, m):
        if abs(i-j) <= k:
            count+=1
    print("YES" if count>=x else "NO")
