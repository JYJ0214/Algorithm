def solution(a, b):
    cla1 = int(str(a) + str(b))
    cla2 = 2 * a * b
    answer = cla1 if cla1 > cla2 else cla2
    return answer