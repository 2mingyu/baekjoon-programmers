function solution(numbers, k) {
    var answer = 0;
    for (let i=0; i<k-1; i++) {
        answer = (answer + 2) % numbers.length;
        console.log(answer);
    }
    return answer+1;
}