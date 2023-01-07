import math

#not able to solve
def andOperator(x, y):
    # Iterate over all bits of y, starting from the lsb, if it's equal to 1, flip it
    for i in range(int(math.log2(y) + 1)):

        # repeat till x >= y, otherwise return the answer
        if (y <= x):
            return y
        if (y & 1 << i):
            y = y & (~(1 << i))
    return y
l = [2, 3, 4, 7]
left_or = 0
for i in range(len(l)):
    l = andOperator()