def solution(arr, intervals):
    first = arr[intervals[0][0] : intervals[0][1] + 1]
    second = arr[intervals[1][0] : intervals[1][1] + 1]
    answer = first + second
    return answer