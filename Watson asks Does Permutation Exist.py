
t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    flag = 0
    for i in range(len(l)-1):
        if abs(l[i] - l[i + 1])>1:
            print("NO")
            flag = 1
            break
    if flag==0:
        print("YES")