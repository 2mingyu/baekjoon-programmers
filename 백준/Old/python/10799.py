"""
쇠막대기
j는 현재 놓인 막대기 수
"""
S=input()
j=r=0
for i in range(len(S)):
 if S[i]=='(':j+=1
 else:
  j-=1
  if S[i-1]=='(':r+=j
  else:r+=1
print(r)