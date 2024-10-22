"""
치즈버거 만들기
"""
A, B = map(int, input().split())
A -= 2
B -= 1
print(min(A, B)*2 + 3)