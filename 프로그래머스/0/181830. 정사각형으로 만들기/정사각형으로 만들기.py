def solution(arr):
    answer = arr
    diff = len(arr) - len(arr[0])
    if diff == 0:
        return arr
    elif diff < 0:
        for _ in range(abs(diff)):
            answer.append([0] * len(arr[0]))
    else:
        for row in answer:
            row += [0] * diff
    return answer