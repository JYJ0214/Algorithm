def solution(s):
    answer = 0
    split_s = s.split()
    for idx, val in enumerate(split_s):
        if val == "Z":
            answer -= int(split_s[idx - 1])
        else:
            answer += int(val)
    return answer
