t = int(input())
for t in range(t):
    n, k = map(int, input().split())

    nMinusOneSum = (n * (n - 1)) // 2

    if k < n / 2:
        nToSwap = n - 2 * k
        nMinusOneSum -= (nToSwap * (nToSwap - 1)) // 2
    print(nMinusOneSum)
