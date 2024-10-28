function solution(n) {
    n = n.replace(/zero/g, "0");
    n = n.replace(/one/g, "1");
    n = n.replace(/two/g, "2");
    n = n.replace(/three/g, "3");
    n = n.replace(/four/g, "4");
    n = n.replace(/five/g, "5");
    n = n.replace(/six/g, "6");
    n = n.replace(/seven/g, "7");
    n = n.replace(/eight/g, "8");
    n = n.replace(/nine/g, "9");
    return Number(n);
}

