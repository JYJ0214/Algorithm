import re


def solution(myStr):
    result = list(filter(lambda x: len(x) != 0, re.split(r"[a-c]", myStr)))
    answer = result if len(result) != 0 else ["EMPTY"]
    return answer
