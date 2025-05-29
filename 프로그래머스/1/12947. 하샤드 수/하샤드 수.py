def solution(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    answer = x % sum == 0
    return answer
