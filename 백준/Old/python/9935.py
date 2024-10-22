"""
문자열 폭발

S = input()
C = input()
stack = ''
for s in S:
    stack += s
    if len(stack) >= len(C):
        if stack[-len(C):] == C:
            stack = stack[:-len(C)]

if stack: print(''.join(stack))
else: print('FRULA')

문자열 슬라이싱이 시간 더 걸리나봄
"""
S = input()
C = input()
stack = []
for s in S:
    stack.append(s)
    if len(stack) >= len(C):
        if ''.join(stack[-len(C):]) == C:
            for _ in range(len(C)): stack.pop()

if stack: print(''.join(stack))
else: print('FRULA')