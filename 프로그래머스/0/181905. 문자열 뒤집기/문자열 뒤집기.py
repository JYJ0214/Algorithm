def solution(my_string, s, e):
    change_str = "".join(list(my_string[s : e + 1])[::-1])
    answer = my_string.replace(my_string[s : e + 1], change_str)
    return answer