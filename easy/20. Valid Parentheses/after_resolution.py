def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    dict = {'(' : ')', '[' : ']', '{' : '}'}
    stack = []
    for iin in s:
        if iin in dict.keys():
            stack.append(iin)
        else:
            if stack == []:
                return False
            a = stack.pop()
            if iin!= dict[a]:
                return False
    return stack == []


print(isValid("({[]})"))