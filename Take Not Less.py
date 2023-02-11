"""
1 2 3 - odd - M
1 1  - same - z
1 0  - odd - m
1 2 2 3 - odd - m
1 1 2 2 3 - odd -m
1 1 2 2 3 3 - same z
"""

t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int, input().split()))[:n]
    dic = {}
    flag = True
    for i in l:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for key, value in dic.items():
        if value & 1 != 0:
            flag = False
            break
    print("Marichka" if flag == False else "Zenyk")
