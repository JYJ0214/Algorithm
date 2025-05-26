def solution(myString: str):
    split_string = myString.split("x")
    answer = list(map(lambda char: len(char), split_string))
    return answer
