def solution(num_list):
    add = 0
    multi = 1

    for num in num_list:
        add += num
        multi *= num

    answer = 1 if multi < (add**2) else 0
    return answer