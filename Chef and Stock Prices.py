

t = int(input())
for t in range(t):
    l = list(map(int, input().split()))
    a = l[0] + (l[0]/100)*l[-1]
    if l[1]<=a<=l[-2]:
        print("Yes")
    else:
        print("No")