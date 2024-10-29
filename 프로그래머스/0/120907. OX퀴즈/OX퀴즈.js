function solution(quiz) {
    var answer = [];
    for (let q of quiz) {
        q = q.split(" ");
        if (q[1] == "+") {
            answer.push(Number(q[0]) + Number(q[2]) == Number(q[4]) ? "O" : "X")
        }
        else if (q[1] == "-") {
            answer.push(Number(q[0]) - Number(q[2]) == Number(q[4]) ? "O" : "X")
        }
    }
    return answer;
}