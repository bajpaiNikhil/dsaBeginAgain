#
#
#
# n = 3
# s = "100100"
# l = []
# for i ,j in enumerate(s):
#     l.append([j,i+1])
# print(l)
# l.sort()
# print(l)
# s1 = ""
# s2 = ""
# result = []
# count=0
# for o in l:
#     if count<n:
#         s1+=o[0]
#         result.append(o[1])
#         count+=1
#     else:
#         s2+=o[0]
# print(*result , s1 , s2)

t = int(input())
for t in range(t):
    n = int(input())
    s = str(input())
    l = []
    for i, j in enumerate(s):
        l.append([j, i + 1])
    l.sort()
    s1 = ""
    s2 = ""
    result = []
    count = 0
    for o in l:
        if count < n:
            s1 += o[0]
            result.append(o[1])
            count += 1
        else:
            s2 += o[0]
    if s1==s2:
        print(-1)
    else:
        print(*result)
#


