"""
Cameras

정규 표현식도 된다는 사실
"""
"""
n = int(input())
number = '123456789'
for _ in range(n):
    s = input()
    if s[0] in number and s[0] == s[1]:
        if s[2] in number and s[3] in number:
            if s[4] not in number and s[4].isupper():
                if s[5] in number and s[6] in number and s[7] in number:
                    print(s)
"""
import re
for _ in range(int(input())):
 s=input()
 if re.fullmatch(r'([1-9])\1[1-9]{2}[A-Z][1-9]{3}',s):print(s)