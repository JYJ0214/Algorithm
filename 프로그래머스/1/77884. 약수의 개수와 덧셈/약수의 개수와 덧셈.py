import math

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        is_square = math.sqrt(i) == int(math.sqrt(i))
        answer += -i if is_square else i
    return answer