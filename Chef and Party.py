

t = int(input())
for t in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    # print(a)
    count = 0
    for i in a:
        if count >= i:
            count += 1
    print(count)
