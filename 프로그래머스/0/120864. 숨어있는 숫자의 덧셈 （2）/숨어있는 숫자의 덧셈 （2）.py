import re

def solution(my_string):
    answer = 0
    regex = r"[a-zA-Z]"
    split_list = re.split(regex, my_string)
    for i in split_list:
        if i.isdigit():
            answer += int(i)
    return answer