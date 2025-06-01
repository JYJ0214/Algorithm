def solution(s):
    sort_list = list(map(int, s.split()))
    answer = f"{min(sort_list)} {max(sort_list)}"
    return answer