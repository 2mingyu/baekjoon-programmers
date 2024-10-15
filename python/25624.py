"""
SNUPTI
"""
N, M = map(int, input().split())
a = [-1] * 26
order = [set() for _ in range(N)]
d = set()
flag = True

for _ in range(M):
    snupti = input()
    if snupti in d:
        flag = False
        continue
    else:
        d.add(snupti)
    if not flag:
        continue
    for n in range(N):
        letter = snupti[n]
        letter_index = ord(letter) - ord('A')
        if a[letter_index] == -1:
            a[letter_index] = n
            order[n].add(letter)
        elif a[letter_index] != n:
            flag = False
            break
    if not flag:
        break

if not flag:
    print("NO")
else:
    total_combinations = 1
    for n in range(N):
        total_combinations *= len(order[n])
    if total_combinations != M:
        print("NO")
    else:
        print("YES")
        for n in range(N):
            print(''.join(sorted(order[n])))