# 01001 < 2번 뒤집으면 원래대로 돌아오는 문제.
input = "010110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    flag = 1
    a_count= 0
    b_count = 0



    for a in range(len(string)-1):
        if (string[a] == string[a+1] == '1'):
            a_count-=1
        if (string[a] == string[a+1] == '0'):
            b_count-=1

    for b in string:
        if b == '1' : a_count +=1
        else : b_count +=1


    return min(a_count,b_count)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)