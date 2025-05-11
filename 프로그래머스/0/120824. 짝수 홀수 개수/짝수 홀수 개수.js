function solution(num_list) {
    const length = num_list.length;
    const even = num_list.filter((value) => value % 2 === 0).length;
    const odd = length - even;
    return [even, odd];
}