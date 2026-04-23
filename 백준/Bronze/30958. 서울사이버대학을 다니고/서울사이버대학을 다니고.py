N = int(input())
s = input()
freq = [0] * 26
for c in s:
    if c.isalpha():
        freq[ord(c) - ord('a')] += 1
print(max(freq))