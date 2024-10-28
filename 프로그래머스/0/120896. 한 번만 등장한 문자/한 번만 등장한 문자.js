function solution(s) {
  const f = {};
  for (let c of s) {
    f[c] = (f[c] || 0) + 1;
  }
  let answer = Object.keys(f).filter(char => f[char] === 1);
  answer.sort();
  return answer.join('');
}