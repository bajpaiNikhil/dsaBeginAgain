

t = int(input())
for t in range(t):
    n = int(input())
    summ = (n*(n+1))/2
    print(summ)
    print(n if summ%2==0 else n-1)