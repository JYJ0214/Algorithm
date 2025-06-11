def solution(arr, queries):
    answer = []
    for query in queries:
        num_list = []
        for num in range(query[0], query[1] + 1):
            if query[2] < arr[num]:
                num_list.append(arr[num])
        if len(num_list) == 0:
            num_list.append(-1)
        answer.append(min(num_list))
    return answer
