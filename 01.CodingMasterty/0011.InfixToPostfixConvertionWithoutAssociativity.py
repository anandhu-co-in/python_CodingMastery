# https://www.geeksforgeeks.org/amazon-interview-experience-sde-1-amazon-wow-2020/?ref=leftbar-rightbar
# 4. Infix to Postfix conversion


def convert(infixExp):
    operators = {
        '^': 10,
        '*': 8,
        '/': 8,
        '+': 6,
        '-': 6
    }

    stack = []
    result = []

    for c in infixExp:
        if c == '(':
            stack.append(c)

        elif c == ')':

            while (True):
                temp = stack.pop()
                if temp == '(': break
                result.append(temp)

        elif (c not in operators):
            result.append(c)

        else:
            while (len(stack)!=0 and stack[len(stack)-1]!="(" and not operators[stack[len(stack) - 1]] < operators[c]):
                result.append(stack.pop())
            stack.append(c)

    while len(stack)!=0:
        result.append(stack.pop())

    return "".join(result)

infix = "a+b*(c^d-e)^(f+g*h)-i"
print(convert(infix))

print("abcd^e-fgh*+^*+i-")