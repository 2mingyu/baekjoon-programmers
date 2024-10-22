"""
모음의 개수
"""
while True:
    s = input()
    if s == '#': break
    else:
        r = 0
        for c in s:
            if c in 'AEIOUaeiou': r += 1
        print(r)