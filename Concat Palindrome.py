# import collections
# from collections import Counter
# a = "abcdd"
# b = "acx"
# dA = dict(collections.Counter(a))
# dB = dict(collections.Counter(b))
# print(dA , dB)
#
# for i in range(len(b)):
#     if b[i] in dA:
#         dA[b[i]]-=1
#         if dA[b[i]] == 0:
#             del dA[b[i]]
#     else:
#         break
# print(dA)


t = int(input())
for t in range(t):
    n, m = map(int, input().split())
    a = input()
    b = input()
    d = {}
    breakFlag = False
    countOddFlag = False
    countOdd = 0
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    for i in range(len(b)):
        if b[i] in d:
            d[b[i]] -= 1
            if d[b[i]] == 0:
                del d[b[i]]
        else:
            breakFlag = True
            break
    for i in d.values():
        if i & 1 != 0:
            print(i)
            countOdd += 1
    print(n+m,countOdd)
    if (((n + m) & 1 == 0 and countOdd == 0) or ((n + m) & 1 != 0 and countOdd == 1) )and breakFlag==False :
        print("YES")
    elif breakFlag:
        print("NO")
    else :
        print("NO")
