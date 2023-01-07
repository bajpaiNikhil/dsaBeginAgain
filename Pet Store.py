t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int, input().split()))[:n]
    if len(l) % 2 != 0:
        print("NO")
    else:
        d = {}
        flag = False
        for i in range(len(l)):
            if l[i] not in d:
                d[l[i]] = 1
            else:
                d[l[i]]+=1
        print(d)
        for i in list(d.values()):
            if i%2 !=0:
                flag  = True
                break
            else:
                flag = False
        if flag :
            print("NO")
        else:
            print("YES")

