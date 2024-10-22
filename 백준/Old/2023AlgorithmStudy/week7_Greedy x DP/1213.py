"""
팰린드롬 만들기

길이가 홀수면
개수가 홀수인 알파벳 하나, 나머지는 개수가 짝수
길이가 짝수면
전부 개수가 짝수
ord('A') = 65
chr(65) = 'A'
"""
A = sorted(list(input()))
Alphabet = [0 for _ in range(26)]
for a in A:
    Alphabet[ord(a) - 65] += 1
odd = -1
for i in range(len(Alphabet)):
    if Alphabet[i] % 2 == 1:
        if odd != -1:
            print('I\'m Sorry Hansoo')
            exit(0)
        else:
            odd = i
left = ''
for i in range(len(Alphabet)):
    left += chr(i + 65) * (Alphabet[i] // 2)
if odd != -1:
    print(left + chr(odd + 65) + left[::-1])
else:
    print(left + left[::-1])