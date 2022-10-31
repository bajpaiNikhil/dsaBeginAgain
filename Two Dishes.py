t = int(input())
for t in range(t):
    l = list(map(int, input().split()))
    if l[1] + l[-1] >= l[0] and l[2] >= l[0]:
        print("Yes")
    else:
        print("No")
