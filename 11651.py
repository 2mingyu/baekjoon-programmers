"""
좌표 정렬하기 2
"""
l = []
for _ in range(int(input())): l.append(list(map(int, input().split())))
l.sort(key=lambda x: (x[1], x[0]))
for i in l: print(i[0], i[1])