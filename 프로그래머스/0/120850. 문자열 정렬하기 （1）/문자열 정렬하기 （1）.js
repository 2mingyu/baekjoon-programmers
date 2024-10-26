function solution(my_string) {
    var answer = [];
    for (let c of my_string) {
        if (!isNaN(c)) {
            answer.push(Number(c));
        }
    }
    return answer.sort((a, b) => a - b);
}