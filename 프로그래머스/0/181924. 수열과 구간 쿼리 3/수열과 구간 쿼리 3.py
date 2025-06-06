def solution(arr, queries):
    answer = list(arr)
    for query in queries:
        copy_arr = list(answer)
        answer[query[0]] = copy_arr[query[1]]
        answer[query[1]] = copy_arr[query[0]]
    return answer
