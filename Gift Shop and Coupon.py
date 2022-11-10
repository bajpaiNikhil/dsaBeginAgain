


t = int(input())
for t in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    count = 0
    sum = 0
    for i in l:
        new_cost = (i+1)//2
        if sum+new_cost<=m:
            count+=1
            sum+=i
        else:
            break
    print(count)
