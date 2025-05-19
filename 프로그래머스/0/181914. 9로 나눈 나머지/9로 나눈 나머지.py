def solution(number):
    answer = 0
    for idx in range(len(number)):
        answer += int(number[idx])
    answer %= 9
    return answer