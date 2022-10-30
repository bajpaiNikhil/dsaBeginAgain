

t = int(input())
for t in range(t):
    l = list(map(int, input().split()))
    if l[1]<=l[0]<=l[2]:
        print("Take second dose now")
    elif l[0]>l[2]:
        print("Too Late")
    elif l[0]<l[1]:
        print("Too Early")
