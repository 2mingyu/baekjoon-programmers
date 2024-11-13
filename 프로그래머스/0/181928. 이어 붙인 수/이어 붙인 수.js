function solution(num_list) {
    let o = 0;
    let e = 0;
    for (let num of num_list) {
        if (num % 2) {
            o = o*10 + num;
        }
        else {
            e = e*10 + num;
        }
    }
    return o + e;
}