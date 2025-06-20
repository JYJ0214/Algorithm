def solution(arr):
    stk = [arr[0]]
    i = 1
    
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
    return stk