function solution(code) {
    let mode = 0;
    let ret = "";
    for (let idx = 0; idx <= code.length - 1; idx++) {
        if (mode == 0) {
            if (code[idx] != "1") {
                if (idx % 2 == 0) {
                    ret += code[idx];
                }
            }
            else if (code[idx] == "1") {
                mode = 1;
            }
        }
        else if (mode == 1) {
            if (code[idx] != "1") {
                if (idx % 2 == 1) {
                    ret += code[idx];
                }
            }
            else if (code[idx] == "1") {
                mode = 0;
            }
        }
    }
    if (ret.length == 0) {
        return "EMPTY";
    }
    return ret;
}