function solution(numbers) {
    const sum = numbers.reduce((acc, cur) => acc + cur, 0);
    const answer = sum / numbers.length;
    return answer;
}