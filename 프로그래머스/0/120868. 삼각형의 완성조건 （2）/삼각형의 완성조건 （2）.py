def solution(sides):
    answer = sides[0] + sides[1] - (abs(sides[0] - sides[1])) - 1
    return answer