
t = int(input())
for t in range(t):
    a = list(map(int,input().split()))
    a.sort()
    if a[-1]>(a[0]+a[1]):
        print("Yes")
    else:
        print("No")