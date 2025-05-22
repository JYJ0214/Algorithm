def solution(num_list):
    condition1 = num_list[-1] - num_list[-2]
    condition2 = num_list[-1] * 2
    next_value = condition1 if num_list[-1] > num_list[-2] else condition2
    num_list.append(next_value)
    return num_list