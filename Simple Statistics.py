


t = int(input())
for t in range(t):
    m , n = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    s = sum(l[n:m-n])/len(l[n:m-n])
    print("%.5f" %s)

