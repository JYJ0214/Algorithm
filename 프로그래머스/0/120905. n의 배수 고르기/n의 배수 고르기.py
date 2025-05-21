def solution(n, numlist):
    answer = list(filter(lambda num: num % n == 0, numlist))
    return answer