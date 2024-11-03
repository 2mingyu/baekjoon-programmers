function solution(sides) {
    [a, b] = sides;
    if (a > b) {
        [a, b] = [b, a];
    }
    let answer = 2*a-1;
    
    return answer;
    
}