function solution(num, total) {
    var answer = [];
    let m = Math.trunc(total / num);
    answer.push(m);
    let i;
    for (i = 1; i <= Math.trunc(num / 2); i++) {
        answer.unshift(m-i);
        answer.push(m+i);
    }
    if (num%2 == 0) {
        answer.shift();
    }
    return answer;
}