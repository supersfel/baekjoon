l = int(input())
str = input()
ls = len(str)
k = [0] *ls
j=0
for i in range(1,ls):
    while j>0 and str[i]!=str[j]:
        j= k[j-1]
    if str[i] == str[j]:
        j+=1
        k[i]=j
print(l-k[-1])