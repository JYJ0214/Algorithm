def solution(rank, attendance):
    answer = 0
    count = 4
    rank_count = 1
    while count >= 0:
        if attendance[rank.index(rank_count)]:
            answer += rank.index(rank_count) * (10**count)
            count -= 2
        rank_count += 1        
        
    return answer