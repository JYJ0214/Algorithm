def solution(my_string):
    answer = list(filter(lambda x: len(x) != 0, my_string.split(" ")))
    return answer