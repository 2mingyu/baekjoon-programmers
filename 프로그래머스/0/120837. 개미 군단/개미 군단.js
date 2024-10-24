function solution(hp) {
    a = Math.trunc(hp/5)
    hp -= a * 5
    b = Math.trunc(hp/3)
    hp -= b * 3
    return a+b+hp;
}