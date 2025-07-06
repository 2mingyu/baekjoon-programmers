b = int(input())
for i in ["Watermelon", "Pomegranates", "Nuts"]:
    if int(input()) <= b:
        print(i)
        exit()
print("Nothing")