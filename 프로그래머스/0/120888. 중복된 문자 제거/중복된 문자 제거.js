function solution(my_string) {
    var answer = '';
    const seen = new Set();

    for (const char of my_string) {
        if (!seen.has(char)) {
            seen.add(char);
            answer += char;
        }
    }
    return answer;
}