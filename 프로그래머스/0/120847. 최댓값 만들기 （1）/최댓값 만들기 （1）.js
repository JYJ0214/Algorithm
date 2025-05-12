function solution(numbers) {
    const sortArr = numbers.sort((a, b) => b - a);
    const answer = sortArr[0] * sortArr[1];
    return answer;
}