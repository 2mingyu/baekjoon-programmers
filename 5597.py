"""
과제 안 내신 분..?
"""
a = [1]*30
for _ in range(28): a[int(input())-1] = 0
for i in range(30):
    if a[i]: print(i+1)