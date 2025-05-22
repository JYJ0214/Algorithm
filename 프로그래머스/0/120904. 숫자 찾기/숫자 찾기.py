def solution(num: int, k):
    str_num = str(num)
    for idx, char in enumerate(str_num):
        if k == int(char):
            return idx + 1
    return -1
