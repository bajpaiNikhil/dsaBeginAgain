t = int(input())
for t in range(t):
    m, n = map(int, input().split())
    k = []
    for i in range(m):
        r1, r2 = list(map(int, input().split()))
        print(k , r1 , r2)
        if r1 <= n:
            k.append(r2)

    print(max(k))
