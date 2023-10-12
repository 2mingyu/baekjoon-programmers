"""
AC
처음엔 R, D 각각 들어올 때 마다 연산 수행해서 시간 초과.
R, D 들어올 때 정보를 reverse, front/back에 저장 후 마지막에 한꺼번에 연산하면 통과
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    p = input().strip()
    input()
    s = input().strip()
    if s == '[]':
        l = []
    else:
        l = s.strip('[').strip(']').split(',')
    r = ''
    front = 0
    back = 0
    reverse = -1
    for c in p:
        if c == 'R':
            reverse = -1 * reverse
        elif c == 'D':
            if reverse == 1:
                back += 1
            else:
                front += 1
    if front + back > len(l):
        print('error')
    else:
        if back == 0:
            l = l[front:]
        else:
            l = l[front:-1*back]
        if reverse == 1:
            l = l[::-1]
        for ll in l:
            r += ll + ','
        print('['+r[:-1]+']')