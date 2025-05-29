import math


def solution(n):
    root = math.sqrt(n)
    answer = (root + 1) ** 2 if root.is_integer() else -1
    return answer