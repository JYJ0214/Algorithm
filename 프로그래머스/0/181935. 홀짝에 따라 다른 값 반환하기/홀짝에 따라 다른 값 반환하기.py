def solution(n):
    if_odd = ((n + 1) ** 2) / 4
    if_even = n * (n + 2) * (2 * n + 2) / 12
    answer = if_odd if n % 2 == 1 else if_even
    return answer
