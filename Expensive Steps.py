t = int(input())
for t in range(t):
    # N X1 Y1 X2 Y2
    l = list(map(int, input().split()))

    a = min(l[1], l[0] - l[1] + 1)
    b = min(l[2], l[0] - l[2] + 1)
    c = min(l[3], l[0] - l[3] + 1)
    d = min(l[4], l[0] - l[4] + 1)
    step = min((abs(l[3] - l[1]) + abs(l[4] - l[2])), (min(c, d) + min(a, b)))
    print(step)
