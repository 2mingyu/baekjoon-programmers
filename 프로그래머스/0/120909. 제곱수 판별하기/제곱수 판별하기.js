function solution(n) {
    return n**(1/2) == Math.trunc(n**(1/2)) ? 1 : 2;
}