def solution(arr):
    count = 1
    while len(arr) > count:
        count *= 2
    answer = arr + [0] * (count - len(arr))
    return answer