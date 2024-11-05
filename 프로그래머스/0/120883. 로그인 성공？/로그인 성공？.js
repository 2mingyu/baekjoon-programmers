function solution(id_pw, db) {
    var answer = 'fail';
    for (let x of db) {
        let [id, pw] = x;
        if (id == id_pw[0]) {
            if (pw == id_pw[1]) {
                return ('login');
            }
            answer = 'wrong pw';
        }
    }
    return answer;
}