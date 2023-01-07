import math

t = int(input())
for t in range(t):
    a, b, c = map(int, input().split())

    if a % b == 0:
        print(-1)
    else:
        if c % a != 0:
            c = (c // a + 1) * a
        while c % b == 0:
            c += a
        print(c)
