
#11233->1-2 ,2-1 ,3-2
#11111

t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int, input().split()))[:n]
    dictionary = {}
    for i in range(len(l)):
        if l[i] not in dictionary:
            dictionary[l[i]]=1
        else:
            dictionary[l[i]]+=1
    b = l[0]
    for i in set(l):
        if dictionary[i]>dictionary[b]:
            b=i
    print(n-dictionary[b])

