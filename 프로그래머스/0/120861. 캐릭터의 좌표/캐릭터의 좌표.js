function solution(keyinput, board) {
    let x = 0;
    let y = 0;
    for (let k of keyinput) {
        if (k == "left") {
            if (x - 1 > -Math.trunc(board[0]/2 + 1)) {
                x -= 1;
            }
        }
        else if (k == "right") {
            if (x + 1 < Math.trunc(board[0]/2 + 1)) {
                x += 1;
            }
        }
        else if (k == "up") {
            if (y + 1 < Math.trunc(board[1]/2 + 1)) {
                y += 1;
            }
        }
        else if (k == "down") {
            if (y - 1 > -Math.trunc(board[1]/2 + 1)) {
                y -= 1;
            }
        }
    }
    return [x, y];
}