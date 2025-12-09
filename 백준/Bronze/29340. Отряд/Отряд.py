a = input()
b = input()
res = ''
for da, db in zip(a, b):
    res+=max(da, db)
print(res)
