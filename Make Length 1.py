t = int(input())
for t in range(t):
    n = int(input())
    s = str(input())
    if n == 1:
        print("Yes")
        break
    for i in range(n - 1):
        if s[i] == "1":
            if (i < n - 1) and (s[i + 1] == "1"):
                i += 1
            else:
                print("No")
                break
    print("Yes")
