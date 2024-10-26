function solution(my_string) {
    var answer = 0;
    for (let c of my_string) {
        if (!isNaN(c)) {
            answer += Number(c);
        }
    }
    return answer;
}