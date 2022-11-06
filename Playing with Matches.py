t = int(input())
for t in range(t):
    dict = {
        "0": 6,
        "1": 2,
        "2": 5,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6
    }

    n, m = map(int, input().split())
    s = str(n + m)
    ans = 0
    for i in s:
        ans += dict[i]
    print(ans)
