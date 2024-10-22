function solution(record) {
    let answer = [];
    let d = {};
    for (let r of record) {
        let rs = r.split(" ");
        if (rs[0] === "Enter" || rs[0] === "Change") {
            d[rs[1]] = rs[2];  // 사용자 ID에 해당하는 닉네임 저장
        }
    }
    for (let r of record) {
        let rs = r.split(" ");
        if (rs[0] === "Enter") {
            answer.push(d[rs[1]] + "님이 들어왔습니다.");
        } else if (rs[0] === "Leave") {
            answer.push(d[rs[1]] + "님이 나갔습니다.");
        }
    }

    return answer;
}
