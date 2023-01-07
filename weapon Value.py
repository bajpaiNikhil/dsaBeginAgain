# 1110001101
# 1010101011
# winner 0 1 0 0 1 0 0 1 1 0
# 0000000011
t = int(input())
for t in range(t):
    n = int(input())
    ll = []
    result = 0
    for j in range(n):
        l = str(input())
        ll.append(l)
    for i in range(10):
        pres_bit = 0
        for j in range(n):
            pres_bit = pres_bit ^ int(ll[j][i])
            #print(j,i , ll[j][i], ord(ll[j][i]) , ord("0"), (ord(ll[j][i]) - ord('0')) , pres_bit ^ (ord(ll[j][i]) - ord('0')))
        # p+=str(pres_bit)
        if pres_bit==1:
            result+=1
        # result += chr((pres_bit) + ord('0'))
    print(result)
