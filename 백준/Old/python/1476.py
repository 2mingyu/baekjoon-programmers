"""
날짜 계산
"""
E,S,M=map(int,input().split())
i=0
while i%15!=E+1 or i%28!=S+1 or i%19!=M+1: i+=1
print(i+1)