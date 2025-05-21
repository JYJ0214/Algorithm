def solution(my_string):
    lower_string_in_list = list(my_string.lower())
    lower_string_in_list.sort()
    answer = "".join(lower_string_in_list)
    return answer
