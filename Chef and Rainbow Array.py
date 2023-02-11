



t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    ans="yes"
    if sum(set(l))!=28 or max(l)!=7:
        ans = "no"
    else:
        left = 0
        right= len(l)-1
        maximum = 1
        while left<right :
            if l[left]!= l[right] or l[left]<maximum:
                ans = "no"
                break
            maximum = max(l[left] , maximum)
            left+=1
            right -=1
    print(ans)

