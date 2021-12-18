s = "(())()"


def is_correct_parenthesis(string):
    # 구현해보세요!
    count = 0
    for n in string:
        if n == '(':
            count +=1
        else :
            count -=1

        if count <0:
            return False

    if count == 0:
        return True
    else :
        return False




print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!