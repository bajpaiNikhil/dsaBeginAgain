
t = int(input())
for t in range(t):
    n = int(input())
    s = input()
    if n == 1 and len(s)==1:
        print("NO")
    elif n==2 and int(s,2)==2:
        print("NO")
    elif s.count("1")>=4:
        print("No")
    else:
        print("YES")
