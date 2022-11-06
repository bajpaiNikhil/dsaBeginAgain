t = int(input())
for t in range(t):
    m = int(input())
    l = list(map(int, input().split()))
    lNum = [1, 2, 3, 4, 5, 6, 7]
    k = 0
    for i in range(m):
        if l[i] in lNum: k += 1
        if k == 7:
            print(i + 1)
            break
