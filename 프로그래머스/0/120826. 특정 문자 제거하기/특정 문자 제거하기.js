function solution(my_string, letter) {
    const answer =  my_string.split('').filter((str) => str !== letter).join('');
    return answer;
}