"""
鉛筆 (Pencils)
"""
N, A, B, C, D = map(int, input().split())
print(min((N//A + bool(N%A)) * B, (N//C + bool(N%C)) * D))