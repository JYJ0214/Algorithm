def solution(price, money, count):
    result = price * count * (count + 1) / 2 - money
    answer = result if result > 0 else 0
    return answer
