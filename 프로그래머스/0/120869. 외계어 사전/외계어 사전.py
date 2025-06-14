def solution(spell, dic):
    join_spell = "".join(sorted(spell))
    sorted_dic = list(map(lambda x: "".join(sorted(x)), dic))
    answer = 1 if join_spell in sorted_dic else 2
    return answer
