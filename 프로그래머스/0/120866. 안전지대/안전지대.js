function solution(board) {
    let n = board.length;
    let newBoard = [];
    for (let i=0; i<n; i++) {
        let tmp = [];
        for (let j=0; j<n; j++) {
            tmp.push(0);
        }
        newBoard.push(tmp);
    }
    for (let i=0; i<n; i++) {
        for (let j=0; j<n; j++) {
            if (board[i][j] == 1) {
                for (let dy of [-1, 0 ,1]) {
                    for (let dx of [-1, 0, 1]) {
                        let ny = i+dy;
                        let nx = j+dx;
                        if (0 <= ny && ny < n && 0 <= nx && nx < n) {
                            newBoard[ny][nx] = 1;
                        }
                    }
                }
            }
        }
    }
    let answer = n*n;
    for (let i=0; i<n; i++) {
        for (let j=0; j<n; j++) {
            answer -= newBoard[i][j];
        }
    }
    return answer;
}