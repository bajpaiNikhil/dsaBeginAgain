

t = int(input())
for t in range(t):
    l = list(map(int, input().split()))
    distance = abs(l[2]-l[0]) + abs(l[3]-l[1])
    if distance%2 == l[-1]%2 and l[-1]>= distance:
        print("Yes")
    else:
        print("No")