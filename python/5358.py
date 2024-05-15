"""
Football Team
"""
while True:
    try:
        s = input()
        n = ''
        for i in range(len(s)):
            if s[i] == 'i': n += 'e'
            elif s[i] == 'e': n += 'i'
            elif s[i] == 'I': n += 'E'
            elif s[i] == 'E': n += 'I'
            else: n += s[i]
        print(n)
    except:
        exit()