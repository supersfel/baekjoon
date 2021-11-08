num = []
for a in range(9):
    num.append(int(input()))

print(max(num))

max_num = max(num)

for a in range(9):
    if num[a] == max_num:
        print(a+1)
        break

