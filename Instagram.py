# a=0
# b=99
# print(f"{a}")
# l=[1,2,3,4]
# for i in range(0,len(l)):
#     print(i)
t = int(input())
for t in range(t):
    n , m = map(int,input().split())
    if m*10<n:
        print("YES")
    else:
        print("NO")
