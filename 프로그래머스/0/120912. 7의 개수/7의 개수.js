function solution(array) {
    var answer = 0;
    for (let c of array.join('')) {
        if (c == 7) {
            answer += 1;
        }
    }
    return answer;
}