function solution(array) {
    const sortArr = array.sort((a, b) => a - b);
    const answer = sortArr[Math.floor(array.length / 2)]
    return answer;
}