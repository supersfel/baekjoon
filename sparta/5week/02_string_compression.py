input = "abcabcabcabcdededededede"


def string_compression(string):
    lst = []
    min_string = len(string)
    for i in range(1,len(string)):
        for j in range(0,len(string),i):
            lst.append(string[j:j+i])


        overlap_lst = []
        for k in range(len(lst)-1):

            if lst[k] == lst[k+1]:
                overlap_lst.append(lst[k])
                lst[k] = ''


        lst = ''.join(lst)

        if min_string>(len(lst) + len(list(set(overlap_lst)))):
            min_string = (len(lst) + len(list(set(overlap_lst))))

        lst =[]

    return min_string


print(string_compression(input))  # 14 가 출력되어야 합니다!



# abcabcab
#
# [a b c a b c a b ] > 8
# [ab ca bc ab]      > 8
# [abc abc ab]       > 6
# [abca bcab]        > 8
# seq[i:i+length] for i in range(0, len(seq), length)
