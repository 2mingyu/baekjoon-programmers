function solution(score) {
    const averages = score.map(s => (s[0] + s[1]) / 2);

    const sorted = [...averages].sort((a, b) => b - a);
    
    return averages.map(avg => sorted.indexOf(avg) + 1);
}