
t = int(input())
for t in range(t):
    n,m = map(int ,input().split())
    l = list(map(int ,input().split()))
    if (n>1 and l[:n-1].count(m)==0) or l.count(m)==0:
        print("No")
    else:
        print("Yes")
