"""
8 3
1 3 2 2 4 1 3 5
3 3 0 1 2 4 1 4

"""
# n, m = 8, 3
# l = [1, 3, 2, 2, 4, 1, 3, 5]
# k = [3, 3, 0, 1, 2, 4, 1, 4]
# a = []
# for i, j in zip(k, l):
#     a.append([i, j])
# print(a)
# a.sort()
# print(a)
# lp = set()
# count = 0
# uniqueCount = 0
# for o in a:
#     print(o)
#     if uniqueCount!=m and o[1] not in lp:
#         count+=o[0]
#         lp.add(o[1])
#         uniqueCount+=1
# print(count)



t = int(input())
for t in range(t):
    n, m = map(int, input().split())
    foodList = list(map(int, input().split()))
    timeList = list(map(int, input().split()))

    if len(set(foodList)) < m:
        print(-1)
    else:
        pairList = []
        for i, j in zip(timeList, foodList):
            pairList.append([i, j])
        pairList.sort()
        k = set()
        count = 0
        uniqueCount = 0
        for o in pairList:
            if uniqueCount!=m and o[1] not in k:
                count+=o[0]
                uniqueCount+=1
                k.add(o[1])
        print(count)




