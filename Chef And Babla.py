import math

t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    maxPositive = math.inf
    maxNegative = -math.inf
    for i in range(len(l)):
        if(l[i]>=0 and l[i]<maxPositive):
            maxPositive=l[i]
        elif (l[i]<0 and l[i]>maxNegative):
            maxNegative=l[i]
    print((min(maxPositive,abs(maxNegative)))-1)



    # positiveList = []
    # negativeList = []
    # if l.count(0)>0:
    #     print(-1)
    # else :
    #     for i in l:
    #         if i >0:
    #             positiveList.append(i)
    #         elif i<0:
    #             negativeList.append(i)
    #     # print(l , len(l))
    #     if len(positiveList)!=0 and len(negativeList)==0:
    #         print(min(positiveList)-1)
    #     elif len(positiveList)==0 and len(negativeList)!=0:
    #         print(abs(max(negativeList)+1))
    #     elif len(positiveList)!=0 and len(negativeList)!=0:
    #         posMax = min(positiveList)-1
    #         negMax = max(negativeList)+1
    #         print(max(posMax,negMax))
    #     else:
    #         print(-1)


# -4 -5 -2
