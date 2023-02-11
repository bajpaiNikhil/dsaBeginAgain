


t = int(input())
for t in range(t):
    l =  list(map(int,input().split()))
    k = l[-1]
    l.sort(reverse=True)
    l.remove(k)
    print("YES" if l[0]+l[1] >= k else "NO")