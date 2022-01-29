t = int(input())
fac =[1]
for i in range(1,501):
    fac.append(fac[-1] * i)


count = 0
for i in reversed(str(fac[t])):
    if i == '0':
        count +=1
    else:
        break

print(count)


