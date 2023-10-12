"""
제로
"""
a=[]
for _ in range(int(input())):
    i=int(input())
    if i:a.append(i)
    else:a.pop()
print(sum(a))