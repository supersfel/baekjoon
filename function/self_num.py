def self_num (num):
    nx_num =num
    for a in str(num):
        nx_num += int(a)
    return nx_num

num = list(range(10000))
for b in range(10000):

    if self_num(b) in num:
        num.remove(self_num(b))

print(*num,sep='\n')
 