def solution(myString):
    answer = ''
    for char in myString:
        answer += "l" if char < "l" else char
    return answer