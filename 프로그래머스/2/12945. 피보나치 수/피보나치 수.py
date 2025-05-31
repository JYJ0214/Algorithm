def solution(n):
    F = [0, 1]
    count = 1

    while count != n:
        count += 1
        F.append(F[-1] + F[-2])
        
    answer = F[-1] % 1234567
    return answer
