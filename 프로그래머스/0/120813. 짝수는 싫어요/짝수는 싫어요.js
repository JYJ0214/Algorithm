function solution(n) {
    let answer = [];
    const point = Math.ceil(n / 2);
    for (let i = 0; i < point; i++) {
        answer.push(1 + 2 * i);
    }
    return answer;
}
