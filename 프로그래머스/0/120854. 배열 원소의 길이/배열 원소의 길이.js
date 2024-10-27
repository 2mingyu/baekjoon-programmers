function solution(strlist) {
    var answer = [];
    while (strlist.length) {
        answer.push(strlist.shift().length);
    }
    return answer;
}