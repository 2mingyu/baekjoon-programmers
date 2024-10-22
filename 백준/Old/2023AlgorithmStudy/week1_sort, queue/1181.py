import sys

n = int(input())
w_list = []
for i in range(n):
    w = sys.stdin.readline().strip()
    if w not in w_list:
        w_list.append(w)
w_list.sort()
w_list.sort(key=len)
for ww in w_list:
    print(ww)