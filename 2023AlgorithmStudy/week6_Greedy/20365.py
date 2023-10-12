"""
블로그2
덩어리 개수가 더 많은 색으로 전체를 칠하고, 나머지 덩어리들 칠하기
group[0]: B덩어리 수
group[1]: R덩어리 수
"""
N = int(input())
p = input()
group = [0, 0]
now = ''
for i in p:
    if i != now:
        if i == 'B': group[0] += 1
        else: group[1] += 1
        now = i
print(1 + min(group))