
t = int(input())
for t in range(t):
    l = list(map(int ,input().split()))
    k = []
    a = l.index(min(l))
    if a == 0:
        print("ALICE")
    elif a == 1:
        print("BOB")
    elif a == 2 :
        print("CHARLIE")
    # for i in l:
    #     k.append((400//i)+1)
    # maxA = k.index(max(k))
    # # print(l)
    # # print(k)
    # # print(maxA)
    # if k[maxA] == k[0]:
    #     print("ALICE")
    # elif k[maxA] == k[1]:
    #     print("BOB")
    # elif k[maxA] == k[2]:
    #     print("CHARLIE")
