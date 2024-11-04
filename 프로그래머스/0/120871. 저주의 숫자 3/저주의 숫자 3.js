function solution(n) {
    var answer = 0;
    for (let i=0; i<n; i++) {
        answer += 1;
        let s = answer.toString();
        while (s.includes('3') || answer % 3 == 0) {
            answer += 1;
            s = answer.toString();
        }
    }
    return answer;
}