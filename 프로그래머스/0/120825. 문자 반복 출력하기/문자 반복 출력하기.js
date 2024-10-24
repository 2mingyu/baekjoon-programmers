function solution(my_string, n) {
    var answer = '';
    for (c of my_string) {
        answer += c.repeat(n);
    }
    return answer;
}