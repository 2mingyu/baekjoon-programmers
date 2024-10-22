"""
양말 짝 맞추기
"""
l = []
for _ in range(5):
    n = input()
    if n in l: l.remove(n)
    else: l.append(n)
print(l[0])