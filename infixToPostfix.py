

def prec(x):
    if x == "*" or "/":
        return 2
    elif x == "+" or "-":
        return 1
    elif x == "^":
        return 3
    else:
        return -1
def infix2prefix(str):
    stack = []
    value = []
    for x in str:
        if x == "(":
            stack.append(x)
        elif x.isalpha():
            value.append(x)
        elif x == ")":
            while len(stack) != 0 and stack[ - 1:] != "(":
                p = stack.pop()
                value.append(p)
            if stack[-1:] == "(":
                stack.pop()
        else:
            while len(stack) != 0 and (prec(x) <= prec(stack[-1:])):
                p = stack.pop()
                value.append(p)
            stack.append(x)
    print(value)
epr = "(a+b)*(c-d)"
infix2prefix(epr)








