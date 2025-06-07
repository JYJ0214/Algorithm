def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            return False

    answer = len(stack) == 0
    return answer
