l = [4, 1, 1, 3]
"""
4 1 1 3
4 1 3

4 2 1 3
3 1 1 2
1 1 2 3
1 2 3 4
0 1 1 1
2 0 1
012
123

3 4 5 6 7 3 1-> 29
1 3 3 4 5 6 7-> 
1 2 3 4 5 6 7 -> 28 
0 1 0 0 0 0 0

1
4
1 3 3 3 o/p -> -1
1 2 2 2
1 2 3 4

"""
# n = 4
# l = [ 3,1,1,2]
# k = [ i for i in range(1,n)]


t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    sumL = (n * (n + 1)) // 2
    sumE = 0
    flag = False
    for i in range(n):
        if l[i] > i + 1:
            flag = True
            break
        sumE += l[i]
    if flag:
        print("-1")
    else:
        print(abs(sumL-sumE))
