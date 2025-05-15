def solution(a, b):
    first = int(str(a) + str(b))
    second = int(str(b) + str(a))
    answer = first if first > second else second
    return answer