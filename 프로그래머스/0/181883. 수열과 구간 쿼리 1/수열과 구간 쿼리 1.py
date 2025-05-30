def solution(arr, queries):
    for query in queries:
        for j in range(query[0], query[1] + 1):
            arr[j] += 1
    return arr
