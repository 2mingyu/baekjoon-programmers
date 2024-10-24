function solution(slice, n) {
    var answer = 0;
    while (answer < n) {
        answer += slice;
    }
    answer /= slice
    return answer;
}