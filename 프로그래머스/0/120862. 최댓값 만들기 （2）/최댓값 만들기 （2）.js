function solution(numbers) {
    const sortNumbers = numbers.sort((a, b) => a - b);
    const maxMulti = sortNumbers[0] * sortNumbers[1];
    const minMulti = sortNumbers[numbers.length - 1] * sortNumbers[numbers.length - 2];
    const answer = maxMulti > minMulti ? maxMulti : minMulti
    return answer;
}