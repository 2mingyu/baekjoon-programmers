"""
영수증
"""
X=int(input())
for _ in range(int(input())):
    a,b=map(int, input().split())
    X-=a*b
if X:print("No")
else:print("Yes")