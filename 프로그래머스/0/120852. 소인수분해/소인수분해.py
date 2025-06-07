import math


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n):
    answer = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            answer.append(i)

    return answer
