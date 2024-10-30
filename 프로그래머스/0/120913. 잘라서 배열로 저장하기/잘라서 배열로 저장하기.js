function solution(my_str, n) {
    var answer = [];
    let tmp = ""
    for (let i=0; i<my_str.length; i++) {
        tmp += my_str[i];
        if (tmp.length == n) {
            answer.push(tmp);
            tmp = ""
        }
    }
    if (tmp.length > 0) {
        answer.push(tmp);
    }
    return answer;
}