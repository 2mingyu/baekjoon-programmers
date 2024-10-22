"""
파일 옮기기
"""
A, B = map(int, input().split())
C, D = map(int, input().split())
print(min(A+D, C+B))