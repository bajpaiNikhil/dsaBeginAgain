t = int(input())
for t in range(t):
    l = list(map(int, input().split()))
    l.sort()
    print(l[-1]+l[-2])
