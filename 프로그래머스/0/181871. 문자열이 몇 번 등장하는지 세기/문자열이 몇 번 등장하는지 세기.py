def solution(myString, pat):
    answer = 0
    idx = 0
    while idx != len(myString):
        try:
            idx = idx + myString[idx:].index(pat) + 1
            answer += 1
        except:
            return answer