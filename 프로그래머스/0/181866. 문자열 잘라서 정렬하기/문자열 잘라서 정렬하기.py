def solution(myString):
    sort_list = sorted(myString.split("x"))
    answer = list(filter(lambda x: x != "", sort_list))
    return answer