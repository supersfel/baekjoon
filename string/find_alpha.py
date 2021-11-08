s = input()

for a in range(97,123):
    if chr(a) in s: print(s.index(chr(a)),end = ' ')
    else : print(-1,end = ' ')




