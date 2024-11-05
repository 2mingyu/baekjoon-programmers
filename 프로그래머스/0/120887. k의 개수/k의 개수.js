function solution(i, j, k) {
    var answer = 0;
    k = String(k);
    for (let n=i; n<=j; n++) {
        for (let x of String(n)){
            if (x == k) {
                answer += 1;
            }
        }
    }
    return answer;
}