function solution(n) {
    var answer = 0;
    while (n) {
        answer += n%10;
        n = Math.trunc(n/10);
    }
    return answer;
}