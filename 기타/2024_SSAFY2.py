"""
3
20 4
58 -15 22 4 33 19 -25 8 52 47 33 41 -21 56 -6 14 -26 11 -14 13
20 1
0 36 42 -29 -5 54 34 -10 19 53 53 18 -36 56 24 2 37 18 -40 -24
20 6
18 -37 15 -18 38 43 -31 -15 -11 27 11 -15 36 -3 -35 6 15 49 32 27

A에서 슬라이딩 윈도우로 B에 합을 넣기
B에서 K칸 이상 떨어진 것과 더해져야 함
"""
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A[0:K])
    B = [S]
    for i in range(N-K):
        S -= A[i]
        S += A[i+K]
        B.append(S)
    answer = -float('inf')
    for i in range(len(B)-K):
        for j in range(i+K, len(B)):
            answer = max(answer, B[i]+B[j])
    print("#%d" % test_case, answer)