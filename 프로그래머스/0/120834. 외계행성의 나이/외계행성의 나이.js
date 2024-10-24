function solution(age) {
    var answer = '';
    for (i of String(age)) {
        answer += String.fromCharCode(Number(i)+97);
    }
    return answer;
}