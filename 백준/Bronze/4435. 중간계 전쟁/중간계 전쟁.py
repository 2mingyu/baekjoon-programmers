T = int(input())
gw = [1, 2, 3, 3, 4, 10]
sw = [1, 2, 2, 2, 3, 5, 10]
for i in range(1, T + 1):
    g = sum(a * b for a, b in zip(map(int, input().split()), gw))
    s = sum(a * b for a, b in zip(map(int, input().split()), sw))
    print(f"Battle {i}:", end=" ")
    if g > s:
        print("Good triumphs over Evil")
    elif s > g:
        print("Evil eradicates all trace of Good")
    else:
        print("No victor on this battle field")