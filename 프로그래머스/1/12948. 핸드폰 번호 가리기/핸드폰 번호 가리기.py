def solution(phone_number):
    star = len(phone_number) - 4
    answer = star * "*" + phone_number[star:]
    return answer