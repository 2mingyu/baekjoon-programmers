function solution(babbling) {
    let answer = 0;
    
    for (let b of babbling) {
        let c = b;
        for (let a of ["aya", "ye", "woo", "ma"]) {
            c = c.split(a).join(' ');
        }
        if (c.trim() === '') {
            answer++;
        }
    }
    
    return answer;
}