import math

t = int(input())
for t in range(t):
    a, b = map(int, input().split())
    if a ==1 or b ==1:
        print(1)
    else:

        print(math.gcd(a,b))