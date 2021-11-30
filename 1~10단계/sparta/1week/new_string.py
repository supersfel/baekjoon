input = "abadabace"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    alphabet_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_array[arr_index] += 1

    non_occurred = []
    for index in range(len(alphabet_array)):
        if alphabet_array[index] == 1:
            non_occurred.append(chr(index + ord('a')))

    for char in string:
        if char in non_occurred:
            return char


    return non_occurred


result = find_not_repeating_character(input)
print(result)