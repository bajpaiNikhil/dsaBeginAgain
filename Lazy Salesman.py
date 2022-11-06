
t = int(input())
for t in range(t):
    m, n = map(int , input().split())
    l = list(map(int , input().split()))[:m]
    l.sort()
    ans = 0
    count = 0
    for i in range(len(l ) -1 ,-1 , -1):
        if ans <n:
            ans +=l[i]
            count+=1
    print(m-count )

# l = [1 , 2 ,3, 4, 5 ,6]
# l.sort()
# for i in range(len(l)-1,-1,-1):
#     print(i , l[i])
