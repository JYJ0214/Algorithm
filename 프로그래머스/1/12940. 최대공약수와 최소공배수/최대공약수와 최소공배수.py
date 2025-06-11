def solution(n, m):
    answer = []
    small_num = min(n, m)
    measure = 1
    for i in range(2, small_num + 1):
        if n % i == 0 and m % i == 0:
            measure = i
    answer = [measure, n * m / measure]
    return answer