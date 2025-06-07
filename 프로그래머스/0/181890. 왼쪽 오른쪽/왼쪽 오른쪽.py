def solution(str_list):
    idx_l = str_list.index("l") if "l" in str_list else len(str_list)
    idx_r = str_list.index("r") if "r" in str_list else len(str_list)
    answer = str_list[:idx_l] if idx_l < idx_r else str_list[idx_r + 1 :]
    return answer