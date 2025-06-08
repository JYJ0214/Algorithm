def solution(n):
    count = 1
    answer = 1
    while count != n:
        answer += 1
        if answer % 3 != 0 and ("3" not in str(answer)):
            count += 1

    return answer
