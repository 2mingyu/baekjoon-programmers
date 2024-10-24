function solution(n) {
    var answer = 0;
    let m = n**0.5
    for (let i=1; i<m; i++) {
        if (!(n%i)) { answer+= 2; }
    }
    if (!(n%m)) { answer++;}
    return answer;
}