function solution(array, n) {
    var answer = 0;
    var d = Infinity;
    while (array.length) {
        let a = array.shift();
        let abs = Math.abs(a-n);
        if (abs < d) {
            answer = a;
            d = abs;
        }
        else if (abs == d) {
            if (a < answer) {
                answer = a;
            }
        }
    }
    return answer;
}