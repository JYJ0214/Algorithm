function solution(my_string) {
    let answer = ''
    for (let str of my_string) {
        addEnd = str === str.toUpperCase() ? str.toLowerCase() : str.toUpperCase();
        answer += addEnd;
    }
    return answer;
}