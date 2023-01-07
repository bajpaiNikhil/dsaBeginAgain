# 1 2 3 4 5
# 1 3 4 5 6
# 1 1 1 1 1
# 1 2 2 2 2
# 2 2 3 3 3
# 3 3 3 4 4
# 4 4 4 4 5
l = [1,1,1,1,1]
print(len(l) , len(set(l)))


t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    if len(set(l))==1:
        print(sum(l)-1)
    else:
        print(max(l))
