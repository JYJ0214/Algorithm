def solution(arr, n):
    answer = []
    len_is_odd = len(arr) % 2 == 1
    for idx, num in enumerate(arr):
        if len_is_odd:
            num += n if idx % 2 == 0 else 0
            answer.append(num)
        else:
            num += n if idx % 2 == 1 else 0
            answer.append(num)
    return answer
