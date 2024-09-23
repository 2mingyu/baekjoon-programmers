"""
대칭 차집합
"""
input()
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A-B) + len(B-A))