def hansu(num):
    count = 0
    for a in range(1,int(num)+1):
        if a<100:
            count +=1
        elif (a//100 + a%10)/2 == (a//10)%10:
            count +=1
    return count

print(hansu(input()))