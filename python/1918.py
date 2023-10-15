"""
후위 표기식
스택스택
"""
stack = []
r = ""
for c in input():
    if c == "(":
        stack.append(c)
    elif c == ")":
        while stack:
            if stack[-1] != "(":
                r += stack.pop()
            else:
                break
        stack.pop()
    elif c in "+-":
        while stack:
            if stack[-1] in "+-*/":
                r += stack.pop()
            else:
                break
        stack.append(c)
    elif c in "*/":
        while stack:
            if stack[-1] in "*/":
                r += stack.pop()
            else:
                break
        stack.append(c)
    else:
        r += c
while stack:
    r += stack.pop()
print(r)