"""
스택 수열

문제 이해부터 빡세다
https://www.youtube.com/watch?v=byCxMbgzEVM
설명이 애매모호하다네
readline 안한 것 때문에 계속 시간초과
"""
import sys
input = sys.stdin.readline

stack = [0]
m = 0
l = []
result = ''
for _ in range(int(input())):
    l.append(int(input()))
for a in l:
    if a < stack[-1]:
        result = 'NO'
        break
    else:
        if a > stack[-1]:
            for i in range(m+1, a+1):
                stack.append(i)
                result += '+\n'
            m = a
        stack.pop()
        result += '-\n'
print(result)