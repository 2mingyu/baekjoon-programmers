"""
국영수
"""
for x in sorted(sorted(sorted(sorted([input().split()for _ in range(int(input()))],key=lambda x:x[0]),key=lambda x:-int(x[3])),key=lambda x:int(x[2])),key=lambda x:-int(x[1])):print(x[0])