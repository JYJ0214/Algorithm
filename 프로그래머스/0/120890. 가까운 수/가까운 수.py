def solution(array, n):
    answer = 0
    difference = float("inf")
    array.sort(reverse=True)
    for i in array:
        if abs(n - i) <= difference:
            answer = i
            difference = abs(n - i)
    return answer