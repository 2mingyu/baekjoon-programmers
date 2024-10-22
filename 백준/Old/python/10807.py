"""
개수 세기
int형으로 안해도 됨
split() 쓰면 알아서 리스트로 들어가니까 list()로 감쌀 필요 없음
근데 int형으로 안하면 시간 더 걸리네
"""
N = input()
ii = input().split()
v = input()
r = 0
for i in ii:
    if i == v: r += 1
print(r)