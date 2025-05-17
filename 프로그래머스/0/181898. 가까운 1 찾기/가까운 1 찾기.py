def solution(arr, idx):
    answer = arr[idx:].index(1) + idx if 1 in arr[idx:] else -1
    return answer
