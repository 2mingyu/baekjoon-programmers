function solution(cards) {
    var answer = 0;
    let boxes = [];
    for (let i = 0; i < cards.length; i++) {
        if (cards[i]) {
            let count = 1;
            let next = cards[i]-1;
            cards[i] = 0;
            while (cards[next]) {
                count += 1;
                let tmp = cards[next];
                cards[next] = 0;
                next = tmp-1;
            }
            boxes.push(count);
        }
    }
    boxes.sort((a, b) => b - a);
    console.log(boxes);
    if (boxes.length > 1) {
        answer = boxes[0] * boxes[1]
    }
    return answer;
}