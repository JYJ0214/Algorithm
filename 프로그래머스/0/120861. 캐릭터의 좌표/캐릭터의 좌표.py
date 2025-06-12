def solution(keyinput, board):
    answer = [0, 0]
    limit_x = (board[0] - 1) / 2
    limit_y = (board[1] - 1) / 2
    for input in keyinput:
        if input == "left" and answer[0] > -limit_x:
            answer[0] -= 1
        elif input == "right" and answer[0] < limit_x:
            answer[0] += 1
        elif input == "up" and answer[1] < limit_y:
            answer[1] += 1
        elif input == "down" and answer[1] > -limit_y:
            answer[1] -= 1
    return answer