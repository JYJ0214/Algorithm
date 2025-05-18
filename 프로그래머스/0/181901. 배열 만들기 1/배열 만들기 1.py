def solution(n, k):
    answer = list(range(1, n + 1))[k - 1::k]
    return answer
