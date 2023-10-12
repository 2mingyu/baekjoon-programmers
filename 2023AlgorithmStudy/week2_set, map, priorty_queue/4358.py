import sys

species = dict()
total = 0
while True:
    tmp = sys.stdin.readline().strip()
    if not tmp:
        break
    else:
        total += 1
        if tmp in species:
            species[tmp] += 1
        else:
            species[tmp] = 1
species = sorted(species.items())
for s in species:
    print("%s" %s[0] , end=" ")
    print("%0.4f"%(s[1] / total * 100))