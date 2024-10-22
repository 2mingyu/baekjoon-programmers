"""
Counting Antibodies
"""
Vk, Jk = map(int, input().split())
Vl, Jl = map(int, input().split())
Vh, Dh, Jh = map(int, input().split())
print(((Vk * Jk) + (Vl * Jl)) * (Vh * Dh * Jh))