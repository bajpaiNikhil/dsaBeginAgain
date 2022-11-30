t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int, input().split()))[:n]
    count = 0
    if l[0] == l[1]:
        count += 1
    if l[n - 2] == l[n - 1]:
        count += 1
    for i in range(1, len(l) - 1):
        if l[i] == l[i - 1] and l[i] == l[i + 1]:
            count += 1
    print(n - count)
