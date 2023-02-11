k = "01101" \
    "010" \
    "000" \
    "" \
    "" \
    "101010" \
    "010101" \
    "0 0101" \
    "00 01" \
    "000"

t = int(input())
for t in range(t):
    n = int(input())
    s = input()
    # print(s.count("1"), s.count("0"))
    if s.count("0") >= s.count("1"):
        print(s.count("1"))
    else:
        print(s.count("0")+1)


