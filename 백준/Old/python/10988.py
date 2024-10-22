"""
팰린드롬인지 확인하기
"""
s = input()
i, j = 0, len(s)-1
while i < j:
    if s[i] != s[j]:
        print(0)
        exit()
    i += 1
    j -= 1
print(1)