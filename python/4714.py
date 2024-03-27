"""
Lunacy
"""
while True:
    X = float(input())
    if X < 0: break
    Y = X * 0.167
    print('Objects weighing %.2f on Earth will weigh %.2f on the moon.' % (X, Y))
