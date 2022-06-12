def KMP(t,p):
    lp = len(p)
    k = [0] * lp

    j=0
    for i in range(1,lp):
        while j>0 and p[i] != p[j]:
            j =k[j-1]
        if p[i]==p[j]:
            j+=1
            k[i] = j
    j=0
    for i in range(1,len(t)):
        while j>0 and t[i] != p[j]:
            j = k[j-1]
        if t[i] == p[j]:
            if j == lp-1:
                return i-lp+1
            else:
                j+=1


while True:
    str = input()
    if str =='.':
        break
    print( len(str) // KMP(str+str,str))
