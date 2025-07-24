import re
print(re.sub(r'(.)\1+',r'\1',input()))