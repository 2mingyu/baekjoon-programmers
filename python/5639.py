"""
이진 검색 트리
"""
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

li = []
while True:
    try:
        li.append(int(input()))
    except:
        break

def f(l):
    if len(l) == 0:
        return
    if len(l) == 1:
        print(l[0])
        return
    root = l[0]
    i = 1
    while i < len(l):
        if l[i] < root:
            i += 1
        else:
            break
    f(l[1:i])
    f(l[i:len(l)])
    print(root)

f(li)