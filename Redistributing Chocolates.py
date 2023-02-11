k = "" \
    "3 2 2" \
    "3 3 2"

t = int(input())
for t in range(t):
    l = list(map(int, input().split()))
    print("YES" if sum(l)>5 else "NO")

