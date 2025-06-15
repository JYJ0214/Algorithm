def solution(id_pw, db):
    for info in db:
        if id_pw[0] != info[0]:
            continue
        elif id_pw[1] != info[1]:
            return "wrong pw"
        else:
            return "login"
    return "fail"