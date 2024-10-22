"""
뉴비의 기준은 뭘까?
"""
N, M = map(int, input().split())
if M < 3: r = "NEWBIE!"
elif M <= N: r = "OLDBIE!"
else: r = "TLE!"
print(r)