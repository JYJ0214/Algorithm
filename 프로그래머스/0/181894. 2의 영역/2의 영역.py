def solution(arr):
    if 2 not in arr:
        return [-1]
    idx1 = arr.index(2)
    idx2 = len(arr) - arr[::-1].index(2)
    answer = arr[idx1 : idx2]
    return answer