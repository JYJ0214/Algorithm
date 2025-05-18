def solution(n):
    answer = ((n + 1) ** 2) / 4 if n % 2 == 1 else n * (n + 2) * (2 * n + 2) / 12
    return answer
