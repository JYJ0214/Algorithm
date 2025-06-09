def solution(ineq, eq, n, m):
    operator = ineq if eq == "!" else f"{ineq}="
    answer = int(eval(f"{n} {operator} {m}"))
    return answer