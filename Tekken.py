


t = int(input())
for t in range(t):
    l = list(map(int,input().split()))
    print("YES" if l[0]>(abs(l[1]-l[2])) else "NO")