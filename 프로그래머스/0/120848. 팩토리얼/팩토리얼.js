function solution(n) {
    var i = 1;
    var f = 1;
    while (true) {
        f *= i;
        if (f > n) {
            return i-1;
        }
        i += 1;
    }
}