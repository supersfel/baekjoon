t = int(input())
str=['0']*t
count_str =[]


for n in range(t):
    str[n]= input()


for i in range(t):
    count = 0
    sum = 0
    for a in str[i]:
        if a == 'O':
            count += 1
            sum += count
        else :
            count = 0
    print(sum)


