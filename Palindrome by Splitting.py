# s = "221424122"
# se = "3764 -> 31664 -> 316613"
# dee = "12345 -> 123441 -> 1234221-> 12214221-> 122131221"
# dfr = "2342->23132"
# ret = "45632->225632 -> 2256122->22146122->221424122"
# print(s == s[::-1], s[::-1])
l = [1, 2, 3, 2, 1]
t = int(input())
for t in range(t):
    n=int(input())
    l = list(map(int,input().split()))[:n]
    left = 0
    right = len(l) - 1
    count = 0
    while left < right:
        if l[left] == l[right]:
            left += 1
            right -= 1
        elif l[left] < l[right]:
            l[right] = l[right] - l[left]
            left += 1
            count += 1
        else:
            l[left] = l[left] - l[right]
            right -= 1
            count += 1
    print(count)
