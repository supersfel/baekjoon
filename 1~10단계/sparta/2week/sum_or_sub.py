numbers = [1, 1, 1,1,1]
target_number = 3



count = 0

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target,oldlst):
    # 구현해보세요!
    if len(array)== 0:
        return oldlst

    num_lst=[]
    for a in oldlst:
        num_lst.append(a + array[0])
        num_lst.append(a - array[0])



    return get_count_of_ways_to_target_by_doing_plus_or_minus(array[1:],3, num_lst )


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number,[0]).count(3))  # 5를 반환해야 합니다!



