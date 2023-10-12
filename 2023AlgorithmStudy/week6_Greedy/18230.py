"""
2xN 예쁜 타일링
2x1에서 가장 예쁜 타일 2개와 2x2에서 가장 예쁜 타일 비교?
N이 홀수면 2x1에서 가장 예쁜 타일 하나는 빼놓기?
"""
N, A, B = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_list.sort()
b_list.sort()
result = 0
if N%2 : result += a_list.pop()
for i in range(N//2):
    if len(a_list) < 2:
        result += b_list.pop()
    elif not b_list:
        result += a_list.pop()
        result += a_list.pop()
    else:
        if a_list[-1] + a_list[-2] > b_list[-1]:
            result += a_list.pop()
            result += a_list.pop()
        else:
            result += b_list.pop()
print(result)