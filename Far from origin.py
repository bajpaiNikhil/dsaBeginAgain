import math

t = int(input())
for t in range(t):
    l = list(map(int,input().split()))
    # l = x1, y1 , x2, y2
    d1 = math.sqrt((l[0]-0)**2 + (l[1]-0)**2)
    d2 = math.sqrt((l[2]-0)**2 + (l[3]-0)**2)
    if d1==d2:
        print("EQUAL")
    elif d1>d2:
        print("ALEX")
    else:
        print("BOB")