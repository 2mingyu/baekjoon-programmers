"""
과목선택
"""
l = [int(input()) for _ in range(6)]
print(sum(l) - min(l[0:4]) - min(l[4:6]))