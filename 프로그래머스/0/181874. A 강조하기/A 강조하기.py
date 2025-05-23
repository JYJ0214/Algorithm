def solution(myString):
    answer = ""
    for char in myString:
        
        answer += "A" if (char == "a" or char == "A") else char.lower()
    return answer