def solution(my_string, n):
    length = len(my_string)
    answer = my_string[length - n:]
    return answer