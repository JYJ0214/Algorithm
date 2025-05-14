def solution(array, height):
    new_arr = array + [height]
    new_arr.sort(reverse=True)
    answer = new_arr.index(height)
    return answer