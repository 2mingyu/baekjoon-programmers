def solution(record):
    answer = []
    d = {}
    for r in record:
        rs = r.split()
        if rs[0] in ["Enter", "Change"]:
            d[rs[1]] = rs[2]
    for r in record:
        rs = r.split()
        if rs[0] == "Enter":
            answer.append(d[rs[1]]+"님이 들어왔습니다.")
        elif rs[0] == "Leave":
            answer.append(d[rs[1]]+"님이 나갔습니다.")
    return answer