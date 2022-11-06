t = int(input())
for t in range(t):
    m, n = map(int, input().split())
    tasteM = 2 * m
    tasteN = 5 * n
    if tasteM > tasteN:
        print("Chocolate")
    elif tasteM < tasteN:
        print("Candy")
    else:
        print("Either")
