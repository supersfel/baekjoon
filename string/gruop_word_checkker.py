T = int(input())
count =0
for t in range(T):
    lst = ['0']
    word = input()
    for a in word:
        if (a != lst[-1]):
            lst.append(a)

    if len(set(word)) == (len(lst) - 1):
        count +=1

print(count)


