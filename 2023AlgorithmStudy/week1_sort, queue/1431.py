import sys

def get_sum(word):
    s = 0
    for w in word:
        if w.isdigit():
            s += int(w)
    return s

n = int(input())
w_list = []
for i in range(n):
    w_list.append(sys.stdin.readline().strip())
w_list.sort()
w_list.sort(key=lambda x:get_sum(x))
w_list.sort(key=len)
for ww in w_list:
    print(ww)