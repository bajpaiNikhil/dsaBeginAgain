t = int(input())
for t in range(t):
    maxTaste, Sum = map(int, input().split())
    if maxTaste>=Sum:
        print(Sum)
    else:
        print(maxTaste-abs(maxTaste-Sum))
