def solution(s: str):
    length = len(s)
    if length % 2 == 0:
        return s[int(length / 2 - 1) : int(length / 2 + 1)]
    else:
        return s[int((length - 1) / 2)]
