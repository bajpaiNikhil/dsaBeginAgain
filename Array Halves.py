l = [3,2,1,4]
n = 2
a = sorted(l)
print(l, a, a[n], a[n - 1])
index = n
target = a[n-1]
result = 0
for i in range(len(l)):
    print(i ,l[i],target)
    if l[i] > target:
        print(i,l[i], index, target, result, index - i)
        result += (index-i)
        index += 1
        # print(i,index,target ,result,index-i)
print(result)

t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    a = sorted(l)
    # print(l, a, a[n], a[n - 1])
    index = n
    target = a[n - 1]
    result = 0
    for i in range(index):
        if l[i] > target:
            result += index - i
            index += 1
    print(result)