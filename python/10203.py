"""
Count Vowels
"""
for _ in range(int(input())):
    s = input()
    r = 0
    for c in s:
        if c in 'aeiou': r += 1
    print(f'The number of vowels in {s} is {r}.')