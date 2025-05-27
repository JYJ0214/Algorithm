def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer += [arr[i]] * arr[i]
    return answer