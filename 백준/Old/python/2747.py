"""
피보나치 수
"""
f=[0,1]
for _ in range(44):f.append(f[-1]+f[-2])
print(f[int(input())])