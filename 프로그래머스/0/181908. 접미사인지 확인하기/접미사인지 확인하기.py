def solution(my_string, is_suffix):
    arr = []
    for idx in range(len(my_string)):
        arr.append(my_string[idx:])
    
    answer = int(is_suffix in arr)
    return answer
    