

#
# from functools import reduce
#
# def factors(n):
#     return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
#
# print(factors(19))

t = int(input())
for t in range(t):
    n = int(input())
    a = 1
    b = 0
    c = 0
    isPrime = False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            b = i
            c = n//i
            isPrime = True
    if not isPrime or b ==c:
        print(-1)
    else:
        print(a,b,c)






    # l = []
    # k = 0
    # if n >5:
    #     n = n%(10**9+1)
    #     for i in range(2, int(n**0.5)+1):
    #         if n % i == 0:
    #             l.append(i)
    #             k += 1
    #         if k == 3:
    #             break
    #     print(l)
    #     if len(l)!=3:
    #         print(-1)
    #     else:
    #         a = l[0]
    #         b = l[1]
    #         c = l[2]
    #         if n % (a * b) == 0 and n % (a * c) == 0 and n % (b * c) == 0 and n%(a*b*c)==0:
    #             print(a, b, c)
    #         else:
    #             print(-1)
    # else:
    #     print(-1)

#
#     # divisor = []
#     # for i in range(2, n + 1):
#     #     while (n % i == 0):
#     #         divisor.append(i)
#     #         n //= i
#     # if (n != 1):
#     #     divisor.append(n)
#     # a = b = c = 1
#     # size = len(divisor)
#     # for i in range(size):
#     #     if a == 1:
#     #         a = a * divisor[i]
#     #     elif b == 1 or b == a:
#     #         b = b * divisor[i]
#     #     else:
#     #         c = c * divisor[i]
#     # if (a == 1 or b == 1 or c == 1
#     #         or a == b or b == c or a == c):
#     #     print("-1")
#     # else:
#     #     print(a, b, c)
#
#
# # n = 3
# # l = []
# # k = 0
# # for i in range(2,n+1):
# #     if n%i==0:
# #         l.append(i)
# #         k+=1
# #     if k == 3:
# #         break
# # print(l)
# # a = l[0]
# # b = l[1]
# # c = l[2]
# # if n%(a*b)==0 and n%(a*c)==0 and n%(b*c)==0:
# #     print(a,b,c)
# # else:
# #     print(-1)
