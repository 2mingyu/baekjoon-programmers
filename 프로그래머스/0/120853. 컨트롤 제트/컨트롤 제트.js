function solution(s) {
    var answer = 0;
    let l = s.split(' ');
    while (l.length) {
        let c = l.pop();
        if (c == 'Z') {
            l.pop();
        }
        else {
            answer += Number(c);
        }
    }
    return answer;
}