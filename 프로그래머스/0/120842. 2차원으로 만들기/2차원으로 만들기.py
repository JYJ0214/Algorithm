def solution(num_list, n):
    answer = [num_list[n * i : (n * (i + 1))] for i in range(int(len(num_list) / n))]
    return answer