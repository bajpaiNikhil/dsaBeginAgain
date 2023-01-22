

l = [0, 1, 2, 3, 4, 5]
xorSum = 0
for i in l:
    xorSum^=i
if xorSum ==0 or len(l)%2!=0:
    print("Yes")
else:
    print("No")