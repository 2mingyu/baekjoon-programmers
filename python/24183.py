"""
Affischutskicket
"""
a, b, c = map(int, input().split())
print('%.6f'%((229*324*a*2 + 297*420*b*2 + 210*297*c) * 0.000001))