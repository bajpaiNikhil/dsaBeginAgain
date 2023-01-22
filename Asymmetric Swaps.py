import math

t = int(input())
for t in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    l = a + b
    l.sort()
    minDiff = l[-1]-l[0]
    # print(minDiff)

    for i in range(len(l) - n):
        # k = l[i:i+n]
        minDiff = min(minDiff , abs(l[i+n-1]-l[i]))
        # print(minDiff , l[i+n-1],l[i],l[i:i+n])
    print(minDiff)
import math

# l =[2, 3, 4, 4, 6, 7, 7, 8, 8, 9]
#
# n = 5
# minDiff= math.inf
# print(l)
# for i in range(len(l)-n+1):
#     # print(i,l[i],l[i+n])
#     # print(l[i:i+n])
#     diff = max(l[i:i+n]) - min(l[i:i+n])
#     print(l[i:i + n],diff , minDiff)
#     minDiff = min(diff,minDiff)
# print(minDiff)
