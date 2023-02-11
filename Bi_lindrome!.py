


t = int(input())
for t in range(t):
    n = int(input())
    s = str(input())
    hasSet = set()
    flag = True
    for i in range(n):
        if s[i] in hasSet:
            flag= False
            break
        hasSet.add(s[i])
    print(n-2 if flag == False else -1)
