def solution(s):
    save = []
    for char in s:
        if save and save[-1] == char:
            save.pop()
        else:
            save.append(char)
    answer = int(len(save) == 0)
    return answer