while True:
    s = input()
    if s == 'EOI': break
    s = s.upper()
    print('Found' if 'NEMO' in s else 'Missing')