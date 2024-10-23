function gcd(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function solution(numer1, denom1, numer2, denom2) {
    var numer3 = numer1 * denom2 + numer2 * denom1;
    var denom3 = denom1 * denom2;
    var g = gcd(numer3, denom3);
    return [numer3 / g, denom3 / g];
}