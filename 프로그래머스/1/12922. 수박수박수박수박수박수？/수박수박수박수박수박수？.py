def solution(n):
    if n % 2 == 0:
        return "수박" * int(n / 2)
    else:
        return "수" + "박수" * int((n - 1) / 2)
