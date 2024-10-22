"""
I Speak TXTMSG
"""
d = {'CU': 'see you',
     ':-)': 'I’m happy',
     ':-(': 'I’m unhappy',
     ';-)': 'wink',
     ':-P': 'stick out my tongue',
     '(~.~)': 'sleepy',
     'TA': 'totally awesome',
     'CCC': 'Canadian Computing Competition',
     'CUZ': 'because',
     'TY': 'thank-you',
     'YW': 'you’re welcome',
     'TTYL': 'talk to you later',
}
while True:
    i = input()
    print(d[i] if i in d else i)
    if i == 'TTYL': break