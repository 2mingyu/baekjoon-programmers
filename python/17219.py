"""
비밀번호 찾기
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
d = dict()
for _ in range(N):
    i = input().split()
    d[i[0]] = i[1]
for _ in range(M):
    print(d[input().strip()])