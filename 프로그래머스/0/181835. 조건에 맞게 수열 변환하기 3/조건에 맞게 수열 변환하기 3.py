def solution(arr, k):
    answer = (
        list(map(lambda num: num * k, arr))
        if k % 2 == 1
        else list(map(lambda num: num + k, arr))
    )
    return answer
