s = input()

if s == '0':
    print(0)
else:
    t = ['000', '001', '010', '011', '100', '101', '110', '111']
    r = [bin(int(s[0], 8))[2:]]
    for c in s[1:]:
        r.append(t[ord(c) - 48])
    print(''.join(r))