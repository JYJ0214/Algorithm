def solution(balls, share):
    def factorial(n):
        return 1 if n <= 1 else n * factorial(n - 1)

    answer = factorial(balls) / (factorial(share) * factorial(balls - share))
    return answer
