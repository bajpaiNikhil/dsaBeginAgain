
t = int(input())
for t in range(t):
    n = int(input())
    odd = []
    even = []

    for i in range(1,n+1):
        if i&1 !=0:
            odd.append(i)
        else:
            even.append(i)
    print(str(odd[::-1]+even)[1:-1].replace(",",""))

n = 10
odd = []
even = []

for i in range(1, n):
    if i & 1 != 0:
        odd.append(i)
    else:
        even.append(i)
print(even, odd)