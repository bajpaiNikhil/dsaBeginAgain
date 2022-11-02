
n = [1,2,3]
# 1 4 6 3 2 5
# 4 6 5
t = int(input())
for t in range(t):
    n , m = map(int,input().split())
    rangeN = n+n
    rangeM = m+m
    print(rangeN,rangeM)
    print(1 if abs(rangeM-rangeN) == 0 else abs(rangeM-rangeN)+1)