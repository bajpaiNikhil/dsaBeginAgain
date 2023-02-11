"""
2 - 2 1
3 - 2 3 1
4 - 2 3 4 1
5 - 2 3 4 5 1
6 - 2%1-0 3%2-1 4%3-1 5%4-1 6%5-1 1%6-0
"""
t = int(input())
for t in range(t):
    n = int(input())
    for i in range(2,n+1):
        print(i,end=" ")
    print(1)
    # s = ""
    # for i in range(2, n + 1):
    #     s += str(i)
    # s += "1"
    # print(s)
    # print("".join(s))
