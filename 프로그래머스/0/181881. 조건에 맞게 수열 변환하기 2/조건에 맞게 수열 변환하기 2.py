def func(x):
    if x >= 50 and x % 2 == 0:
        return x / 2
    elif x < 50 and x % 2 == 1:
        return x * 2 + 1
    else:
        return x


def solution(arr):
    answer = 0
    arr_before = list(arr)
    arr_after = list(map(func, arr))

    while arr_before != arr_after:
        answer += 1
        arr_before = list(arr_after)
        arr_after = list(map(func, arr_after))

    return answer