function solution(lines) {
  const count = new Array(201).fill(0);

  lines.forEach(([start, end]) => {
    for (let i = start + 100; i < end + 100; i++) {
      count[i]++;
    }
  });

  const answer = count.reduce((acc, c) => acc + (c > 1 ? 1 : 0), 0);

  return answer;
}
