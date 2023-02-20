t = int(input())
for t in range(t):
    n = int(input())
    s = input()
    count = 0
    l = []
    for i in range(len(s)):
        if s[i] != "0":
            l.append(i)
    if len(l) == 1:
        print("0")
    elif len(l) == 0:
        print(len(s))
    else:
        for j in range(len(l) - 1):
            if s[l[j]] != s[l[j + 1]] and (abs(l[j] - l[j + 1]) - 1) & 1 != 0:
                count += 1
        print(count)
