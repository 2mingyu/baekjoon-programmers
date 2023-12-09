"""
에디터
"""
import sys
input = sys.stdin.readline

left = list(input().split()[0])
right = []
M = int(input())
for _ in range(M):
    command = input().split()
    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])

print("".join(left+right[::-1]))
