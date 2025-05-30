def solution(before, after):
    answer = int("".join(sorted(list(before))) ==  "".join(sorted(list(after))))
    return answer