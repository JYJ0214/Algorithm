def solution(A,B):
    answer = 0
    sort_A = sorted(A)
    reverse_B = sorted(B, reverse=True)
    for i in range(len(A)):
        answer += sort_A[i] * reverse_B[i]

    return answer
