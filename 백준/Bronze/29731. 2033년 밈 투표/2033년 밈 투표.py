for _ in range(int(input())):
    if input() not in ['Never gonna ' + x for x in ['give you up', 'let you down', 'run around and desert you', 'make you cry', 'say goodbye', 'tell a lie and hurt you', 'stop']]:
        print('Yes')
        exit()
print('No')