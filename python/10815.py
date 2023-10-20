"""
숫자 카드
"""
N = int(input())
s = set(map(int, input().split()))
M = int(input())
for n in list(map(int, input().split())):
    if n in s: print(1, end=" ")
    else: print(0, end=" ")