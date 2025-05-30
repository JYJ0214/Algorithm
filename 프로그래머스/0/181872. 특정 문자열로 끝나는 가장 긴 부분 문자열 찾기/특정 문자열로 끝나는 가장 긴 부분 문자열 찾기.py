def solution(myString, pat):
    reverse_string = myString[::-1]
    reverse_pat = pat[::-1]
    idx = len(myString) - reverse_string.index(reverse_pat)
    answer = myString[:idx]
    return answer
