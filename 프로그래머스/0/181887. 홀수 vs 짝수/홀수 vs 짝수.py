def solution(num_list):
    odd_sum = 0
    even_sum = 0
    for idx, num in enumerate(num_list):
        if idx % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    answer = even_sum if even_sum > odd_sum else odd_sum
    return answer