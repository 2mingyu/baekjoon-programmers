function solution(chicken) {
    var answer = 0;
    let coupon = chicken;
    while (coupon >= 10) {
        chicken = Math.trunc(coupon / 10)
        coupon = coupon - chicken * 10 + chicken;
        answer += chicken;
    }
    return answer;
}