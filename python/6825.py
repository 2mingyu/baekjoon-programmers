"""
Body Mass Index
"""
BMI = float(input()) / float(input()) ** 2
if BMI < 18.5: print('Underweight')
elif BMI > 25: print('Overweight')
else: print('Normal weight')