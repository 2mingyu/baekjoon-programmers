l = input().split('.')
for i in range(len(l)):
    e = l[i]
    if len(e):
        if len(e) % 2:
            print(-1)
            exit()
        else:
            n = 'AAAA'*(len(e)//4)
            if len(e) % 4:
                n += 'BB'
            l[i] = n
print('.'.join(l))