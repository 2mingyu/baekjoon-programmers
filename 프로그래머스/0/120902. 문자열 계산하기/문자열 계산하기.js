function solution(my_string) {
    let l = my_string.split(" ");
    var answer = Number(l.shift());
    while (l.length > 0) {
        if (l.shift() == "+") {
            answer += Number(l.shift());
        }
        else {
            answer -= Number(l.shift());
        }
    }
    return answer;
}