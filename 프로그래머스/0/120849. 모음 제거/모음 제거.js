function solution(my_string) {
    var answer = '';
    for (let c of my_string) {
        if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
            answer += c;
        }
    }
    return answer;
}