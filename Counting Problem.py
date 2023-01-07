



t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    # odd= []
    count = 0
    for i in l:
        if i%2:
            # print(i)
            count+=1
            # odd.append(i)
    # print(odd , count)
    print("NO" if (count%2 or count==0) else "YES")
