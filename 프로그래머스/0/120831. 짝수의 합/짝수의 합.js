function solution(n) {
    const nOfHalf = Math.floor(n / 2);
    const answer = nOfHalf * (nOfHalf + 1);
    return answer;
}