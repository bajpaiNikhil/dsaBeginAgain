t = int(input())
for t in range(t):
    l = list(map(int , input().split()))
    diff = l[1] - l[0]
    w1 = l[2]*l[-1]
    w2 = l[3]*l[-1]
    if w1<=diff<=w2:
        print("1")
    else:
        print("0")