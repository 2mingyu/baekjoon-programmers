function solution(my_string) {
    let answer = 0;
    let t = '';
    for (let c of my_string) {
        if (Number(c) == c) {
            t += c;
        }
        else {
            answer += Number(t);
            t = '';
        }
    }
    answer += Number(t);
    return answer;
}