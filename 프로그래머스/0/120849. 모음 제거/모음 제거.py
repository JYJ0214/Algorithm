def solution(my_string):
    vowel_list = ["a", "e", "i", "o", "u"]
    answer = ""
    for char in my_string:
        if char not in vowel_list:
            answer += char
    return answer
