function solution(dots) {
    const x = dots.map(d => d[0]);
    const y = dots.map(d => d[1]);
    return (Math.max(...x) - Math.min(...x)) * (Math.max(...y) - Math.min(...y))
}