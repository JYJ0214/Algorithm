def solution(n):
    answer = n + 1
    binary = bin(n)
    while binary.count("1") != bin(answer).count("1"):
        answer += 1
    return answer
