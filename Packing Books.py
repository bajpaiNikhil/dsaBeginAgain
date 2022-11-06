t = int(input())
for t in range(t):
    a, b, c = map(int, input().split())
    print(a if c >= b else a * (b // c) if b % c == 0 else a * (b // c + 1))
