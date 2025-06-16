def solution(s):
    answer = ""
    idx = True
    
    for char in s:
        if char != " ":
            if idx:
                answer += char.upper()
            else:
                answer += char.lower()
            idx = not idx
        else:
            answer += " "
            idx = True    
    return answer