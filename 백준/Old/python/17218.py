"""
비밀번호 만들기

예제 찾기
https://www.acmicpc.net/board/view/37132

A, B = input(), input()
start_A, start_B, end_A, end_B = 0, 0, 0, 0
r = ""
do_something = True
while do_something:
    do_something = False
    # print("A: ", A[start_A:end_A+1], start_A, end_A)
    # print("B: ", B[start_B:end_B+1], start_B, end_B)
    for i in range(min(start_A, start_B), max(end_A,end_B)+1):
        if start_A <= i <= end_A:
            # print("i, A[i], B[end_B]", i, A[i], B[end_B])
            if A[i] == B[end_B]:
                r += A[i]
                start_A = i+1
                start_B = end_B+1
                do_something = True
                break
        if start_B <= i <= end_B:
            # print("i, B[i], A[end_A]", i, B[i], A[end_A])
            if B[i] == A[end_A]:
                r += B[i]
                start_B = i+1
                start_A = end_A+1
                do_something = True
                break
    if end_A < len(A)-1:
        end_A += 1
        do_something = True
    if end_B < len(B)-1:
        end_B += 1
        do_something = True
    if start_A > end_A: break
    if start_B > end_B: break
print(r)

예제는 다 맞는데 통과가 안돼 ..

https://junchive.kr/2023-06-04-%EB%B0%B1%EC%A4%80-17218/
A, B = input(), input()
이라고 하면 '출력 형식이 잘못되었습니다'
"""
A = input()
B = input()
LCS = [['']*(len(B)+1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + A[i-1]
        else:
            if len(LCS[i-1][j]) > len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]

print(LCS[len(A)][len(B)])