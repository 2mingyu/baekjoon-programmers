"""
나이 계산하기
"""
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
print(int(m2 > m1 or (m2 == m1 and d2 >= d1)) + y2 - y1 - 1)
print(y2 - y1 + 1)
print(y2 - y1)