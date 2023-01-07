

t = int(input())
for t in range(t):
    l = list(map(int,input().split()))
    if l[0]>l[1]:
        if l[0]-l[-1] > l[1]:
            print("NO")
        else:
            print("YES")
    elif l[0]<l[1]:
        if l[0]+l[2] > l[1]:
            print("YES")
        else:
            print("NO")
    else :
        print("YES")
