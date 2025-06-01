def solution(array):
    join_str = "".join(map(str, array))
    answer = join_str.count("7")
    return answer