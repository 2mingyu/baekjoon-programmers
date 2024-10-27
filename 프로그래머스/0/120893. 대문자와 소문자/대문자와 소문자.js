function solution(my_string) {
    var answer = '';
    let l = my_string.split('');
    while (l.length) {
        let char = l.shift();
        if (char == char.toUpperCase()) {
            answer += char.toLowerCase();
        } else {
        answer += char.toUpperCase();
        }
    }
    return answer;
}