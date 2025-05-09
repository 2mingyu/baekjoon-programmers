try:
    while True:
        o = input()
        d = o.split()
        n = o.split()
        s = set(d)
        e = []
        for i in range(len(d)):
            if d[i] == 'dip' and not ((i > 0 and d[i-1] == 'jiggle') or (i > 1 and d[i-2] == 'jiggle') or (i < len(d)-1 and d[i+1] == 'twirl')):
                if 1 not in e: e.append(1)
                n[i] = 'DIP'
        if d[-3:] != ['clap', 'stomp', 'clap']:
            e.append(2)
        if 'twirl' in s and 'hop' not in s:
            e.append(3)
        if d[0] == 'jiggle':
            e.append(4)
        if 'dip' not in s:
            e.append(5)
        if len(e) == 0:
            print('form ok:', o)
        elif len(e) == 1:
            print(f'form error {e[0]}:', ' '.join(n) if e[0] == 1 else o)
        else:
            se = list(map(str, e))
            k = ', '.join(se[:-1]) + ' and ' + se[-1]
            print(f'form errors {k}:', ' '.join(n) if e[0] == 1 else o)
except:
    exit(0)