function solution(A, B) {
    A = A.split('');
    for (let i = 0; i < A.length; i++) {
        console.log(A.join(''))
        if (A.join('') == B) {
            return i;
        }
        A.unshift(A.pop());
    }
    return -1;
}