t = int(input())
for t in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    bitWiseOr = 0
    for i in l:
        bitWiseOr |= i
    or_result = k - bitWiseOr
    if (or_result & k) == or_result:
        print(or_result)
    else:
        print(-1)
