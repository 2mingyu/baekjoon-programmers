"""
진주로 가자! (Hard)
"""
import sys
input = sys.stdin.readline
N = int(input())
l = [0] * 1002
t = 0
for _ in range(N):
    D, C = input().split()
    if D == 'jinju': f = int(C)
    l[min(int(C), 1001)] += 1
print(f)
print(sum(l[f+1:]))