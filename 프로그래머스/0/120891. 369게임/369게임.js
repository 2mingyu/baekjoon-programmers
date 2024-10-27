function solution(order) {
  return String(order).split('').filter(char => ['3', '6', '9'].includes(char)).length;
}