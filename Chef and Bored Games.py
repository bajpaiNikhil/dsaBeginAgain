
t = int(input())
for t in range(t):
    n = int(input())
    count = 0
    for i in range(1,n+1,2):
        k = (n-i+1)
        count+=(k**2)
    print(count)


n = 8
count = 0
for i in range(1, n + 1, 2):
    print(i)
    k = (n - i + 1)
    count += (k ** 2)
print(count)