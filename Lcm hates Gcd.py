import math

# print(math.gcd(12,15))
# print(math.lcm(12,3),math.gcd(15,3))
t = int(input())
for t in range(t):
    a,b = map(int,input().split())
    k = math.gcd(a,b)
    print(math.lcm(a,k)-math.gcd(b,k))
