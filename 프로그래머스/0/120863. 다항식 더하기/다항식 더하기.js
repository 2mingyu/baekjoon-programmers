function solution(polynomial) {
    let l = polynomial.split(" + ");
    let x = 0;
    let c = 0;
    for (let e of l) {
        if (e[e.length-1] == "x") {
            if (e.length == 1) {
                x += 1;
            }
            else {
                x += Number(e.slice(0, e.length-1));
            }
        }
        else {
            c += Number(e);
        }
    }
    let answer = [];
    
    if (x > 0) {
        if (x == 1) {
            answer.push("x");
        } else {
            answer.push(String(x) + "x");
        }
    }
    
    if (c > 0) {
        answer.push(String(c));
    }
    
    return answer.join(" + ");
}