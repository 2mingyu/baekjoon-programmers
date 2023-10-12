"""
알파벳 개수
"""
a = [0] * 26
for i in input(): a[ord(i)-97] += 1
for i in a: print(i, end=" ")