t = int(input())
student = [0]*t

for a in range(t):
    student[a] = list(map(int,input().split()))
    del student[a][0]

for b in range(t):
    avr = sum(student[b])/len(student[b])
    sum_student =0
    for c in student[b]:
        if c > avr:
            sum_student +=1

    #print('%s%%' %(sum_student/len(student[b]) * 100))
    print("{:.3f}%".format(sum_student*100/len(student[b])))

