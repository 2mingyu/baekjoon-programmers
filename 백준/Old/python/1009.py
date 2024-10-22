"""
분산처리

맨 뒷자리만 봄
a = 1 이면 b 상관 없이 1
a = 2 면 2 4 8 6 반복
a = 3 이면 3 9 7 1 반복
a = 4 이면 4 6 반복
a = 5, 5
a = 6, 6
a = 7, 7 9 3 1
a = 8, 8 4 2 6
a = 9, 9 1
a = 0, 0
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b = map(int, input().split())
    a %= 10
    if a == 0: print(10)
    elif a == 1: print(1)
    elif a == 2: print('6248'[b%4])
    elif a == 3: print('1397'[b%4])
    elif a == 4: print('64'[b%2])
    elif a == 5: print(5)
    elif a == 6: print(6)
    elif a == 7: print('1793'[b%4])
    elif a == 8: print('6842'[b%4])
    elif a == 9: print('19'[b%2])