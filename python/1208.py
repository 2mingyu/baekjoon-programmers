"""
부분수열의 합 2

1182 참고
중간에서 만나기..
dict의 key는 부분수열의 합, value는 key를 만들어내는 경우의 수
"""
import sys
sys.setrecursionlimit(10**6)

N, S = map(int, input().split())
A = list(map(int, input().split()))
left = A[:N//2]
right = A[N//2:]
left_d = dict()
right_d = dict()

def left_f(s, i):
    if i == len(left):
        if s in left_d: left_d[s] += 1
        else: left_d[s] = 1
        return
    left_f(s, i+1)
    left_f(s+left[i], i+1)

def right_f(s, i):
    if i == len(right):
        if s in right_d: right_d[s] += 1
        else: right_d[s] = 1
        return
    right_f(s, i+1)
    right_f(s+right[i], i+1)

left_f(0, 0)
right_f(0, 0)

r = 0
for k in left_d:
    if S-k in right_d:
        r += left_d[k] * right_d[S-k]

if S == 0: r -= 1
print(r)