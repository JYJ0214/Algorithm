function solution(n) {
    let answer = 0;
    const str = String(n);
    for (let value of str) {
        answer += Number(value);
    }
    return answer;
}