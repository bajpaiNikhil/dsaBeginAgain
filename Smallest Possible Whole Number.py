t = int(input())
for t in range(t):
    m, n = map(int, input().split())
    if n == 0:
        print(m)
    else:
        print(m % n)
