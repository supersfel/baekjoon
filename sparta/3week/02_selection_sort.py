#선택정렬을 사용하여 정렬하는 문제
#시간복잡도는 5의 n제곱
input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!

    for i in range(len(array) - 1):
        min_index = i
        for j in range(len(array) - i):
            if array[i+j] < array[min_index]:
                min_index = i+j
                array[i],array[min_index] = array[min_index],array[i]




    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!