function solution(my_string, num1, num2) {
    const strArr = my_string.split('');
    const first = strArr[num1];
    const second = strArr[num2];
    strArr[num1] = second;
    strArr[num2] = first;
    const answer = strArr.join('');
    return answer;
}