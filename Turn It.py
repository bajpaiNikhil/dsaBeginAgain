import math

t = int(input())
for t in range(t):
    l = list(map(int, input().split()))
    v = l[0]**2 - 2*l[2]*l[3]
    print(v*v)
    if v <= l[1]**2:
        print("Yes")
    else:
        print("No")
    # if l[0]==l[1]:
    #     print("Yes")
    # else:
    #     v = math.sqrt((l[0] * l[0]) - 2*l[2]*l[3])
    #     if v <= l[1]:
    #         print("Yes")
    #     else:
    #         print("No")