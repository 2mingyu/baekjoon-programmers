"""
출석 이벤트
"""
N = int(input())
P = int(input())
r = P
if N >= 5: r = min(r, P-500)
if N >= 10: r = min(r, P*0.9)
if N >= 15: r = min(r, P-2000)
if N >= 20: r = min(r, P*0.75)
print(int(max(r, 0)))