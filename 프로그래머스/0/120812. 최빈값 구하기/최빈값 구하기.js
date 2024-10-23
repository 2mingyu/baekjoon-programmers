function solution(array) {
    let n = new Array(1000).fill(0);
    for (let e of array) {
        n[e] += 1;
    }
    
    let t = [];
    let m = -1;
    
    for (let i = 0; i < 1000; i++) {
        if (n[i] > m) {
            t = [i];
            m = n[i];
        } else if (n[i] === m) {
            t.push(i);
        }
    }
    
    if (t.length === 1) {
        return t[0];
    }
    return -1;
}