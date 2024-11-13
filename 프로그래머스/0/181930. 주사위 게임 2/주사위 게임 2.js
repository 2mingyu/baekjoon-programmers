function solution(a, b, c) {
    var answer = a + b + c;
    if (a == b || b == c || c == a) {
        answer *= a**2 + b**2 + c**2;
    }
    if (a == b && b == c) {
        answer *= a**3 + b**3 + c**3;
    }
    return answer;
}