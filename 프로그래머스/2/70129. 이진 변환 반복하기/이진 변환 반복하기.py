def solution(s):
    count = 0
    remove_zero = 0
    while s != "1":
        count += 1
        count_one = s.count("1")
        remove_zero += len(s) - count_one
        s = bin(count_one)[2:]
    answer = [count, remove_zero]
    return answer
