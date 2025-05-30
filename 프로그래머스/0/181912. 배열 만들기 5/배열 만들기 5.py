def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        slice_num = int(i[s : s + l])
        if k < slice_num:
            answer.append(slice_num)
    return answer
