t = int(input())
for t in range(t):
    a,b,c,d = map(int,input().split())
    l = [i for i in range(a,b+1)]
    l2 = [j for j in range(c,d+1) if j not in l]
    print(len(l+l2))