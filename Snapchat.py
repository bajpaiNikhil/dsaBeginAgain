

t = int(input())
for t in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    currentCount = 0
    globalCount =0
    for i,j in zip(a,b):
        # print(i,j)
        if i!=0 and j!=0:
            currentCount+=1
            globalCount=max(globalCount,currentCount)
        else:
            currentCount=0
    print(globalCount)