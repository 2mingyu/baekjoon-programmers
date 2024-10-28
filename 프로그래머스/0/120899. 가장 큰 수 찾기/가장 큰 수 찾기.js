function solution(array) {
    var answer = [-1, -1];
    for (let i=0; i<=array.length; i++) {
        if (Number(array[i]) > answer[0]) {
            answer = [Number(array[i]), i];
        }
    }
    return answer;
}