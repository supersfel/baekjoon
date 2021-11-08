
sum =1
count_sum=[0]*10


for a in range(3):
    sum *= int(input())

for b in str(sum):
    count_sum[int(b)] += 1

for c in range(10):
    print(count_sum[c])



