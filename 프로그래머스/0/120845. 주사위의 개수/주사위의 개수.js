function solution(box, n) {
    const answer = box.map((value) => Math.floor(value / n)).reduce((acc, cur) => acc * cur, 1);
    return answer;
}