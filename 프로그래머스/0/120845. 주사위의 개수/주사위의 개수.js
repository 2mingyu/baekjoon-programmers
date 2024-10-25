function solution(box, n) {
    var answer = 1;
    for (let i=0; i<3; i++) { answer *= Math.trunc(box[i]/n); }
    return answer;
}