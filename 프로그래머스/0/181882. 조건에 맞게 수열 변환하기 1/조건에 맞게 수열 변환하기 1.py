def solution(arr: list):
    def transFunc(num):
        if num >= 50 and num % 2 == 0:
            return num / 2
        elif num < 50 and num % 2 == 1:
            return num * 2
        else:
            return num

    answer = list(map(transFunc, arr))
    return answer
