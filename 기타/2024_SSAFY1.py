"""
3
4 2
1 5 5 3
4 1
3 3 3 3
4 3
2 3 4 4
"""
from collections import deque

def check_same():
    return len(set(A)) == 1

def check_in():
    for record in records:
        if list(A) == record:
            return True
    return False

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = deque(map(int, input().split()))
    answer = 0
    if check_same():
        print("#%d 0" % test_case)
        continue
    records = [list(A)]
    while True:
        answer += 1
        A.append(A[K-1])
        A.popleft()
        if check_same():
            print("#%d" % test_case, answer)
            break
        if check_in():
            print("#%d" % test_case, -1)
            break
        records.append(list(A))