def solution(myString, pat):
    change_str = ""
    for char in myString:
        change_str += "A" if char == "B" else "B"

    answer = int(pat in change_str)
    return answer