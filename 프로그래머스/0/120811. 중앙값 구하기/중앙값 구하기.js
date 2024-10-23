function solution(array) {
    array.sort((a, b) => a - b);
    return array[Math.trunc(array.length / 2)];
}