function solution(num_list) {
    let sum = 0;
    let mul = 1;
    for (let num of num_list) {
        sum += num;
        mul *= num;
    }
    return Number(sum**2 > mul);
}