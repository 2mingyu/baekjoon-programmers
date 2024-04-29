"""
Archivist
"""
i = int(input())
r = "SPbSU"
if i not in [1996, 1997, 2000, 2007, 2008, 2013, 2018]:
    r = ""
    if i == 2006: r = "PetrSU, "
    r += "ITMO"
print(r)