def solution(myString, pat):
    lower_myString = myString.lower()
    lower_pat = pat.lower()
    answer = 1 if lower_pat in lower_myString else 0
    return answer