function solution(array) {
    const maxNum = Math.max(...array);
    const index = array.indexOf(maxNum);
    const answer = [maxNum, index];
    return answer;
}