num = []
for a in range(10):
    num.append(int(input()) % 42  )

num = set(num)
print(len(num))