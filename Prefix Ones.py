

t = int(input())
for t in range(t):
    n = int(input())
    s = input()
    i = s.find("0")
    if i == -1:
        print(len(s))
    else:
        t = s[i:]
        maxLenOnes = 0
        for j in t.split("0"):
            # print(maxLenOnes,len(j))
            maxLenOnes = max(maxLenOnes, len(j))
        print(maxLenOnes + i)




# s = "1101101"
# i = s.find("0")
# if i ==-1:
#     print(len(s))
# else:
#     t = s[i:]
#     maxLenOnes=0
#     for j in t.split("0"):
#         # print(maxLenOnes,len(j))
#         maxLenOnes= max(maxLenOnes,len(j))
#     print(maxLenOnes+i)