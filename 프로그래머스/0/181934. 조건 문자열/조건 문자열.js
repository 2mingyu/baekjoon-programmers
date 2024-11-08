function solution(ineq, eq, n, m) {
    let x = ineq+eq;
    let y;
    if (x == ">=") {
        y = n >= m;
    }
    else if (x == "<=") {
        y = n <= m;
    }
    else if (x == ">!") {
        y = n > m;
    }
    else {
        y = n < m;
    }
    return Number(y);
}