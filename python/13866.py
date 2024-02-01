"""
팀 나누기
"""
A, B, C, D = map(int, input().split())
l = [A+B-C-D, A+C-B-D, A+D-B-C, B+C-A-D, B+D-A-C, C+D-A-B]
print(min([abs(i) for i in l]))