def prefixToPostfix(s):

    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    s = s[::-1] #https://www.geeksforgeeks.org/python-list-comprehension-and-slicing/
    for i in s:

        if i in operators:
            # pop 2 elements from stack
            a = stack.pop()
            b = stack.pop()

            # concatenate them as operand1 + operand2 + operator
            temp = a + b + i  # string = operand1 + operand2 + operator
            stack.append(temp)
        # else if operand
        else:
            stack.append(i)

    print("Converted Prefix Directly to Postfix : ",end='')
    return stack.pop()


#Same as prefix to post fix, except we dont nedd to reverse the array ans also its opera+oparand2+operand1
def postfixToPrefix(s):

    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for i in s:

        if i in operators:
            # pop 2 elements from stack
            a = stack.pop()
            b = stack.pop()

            # concatenate them as operand1 + operand2 + operator
            temp = i + b + a  #string = operator + operand2 + operand1
            stack.append(temp)
        # else if operand
        else:
            stack.append(i)

    print("Converted Postfix Directly to Prefix : ",end='')
    return stack.pop()

s = "*-A/BC-/AKL"

print("Original Prefix : {}".format(s))


postfix=prefixToPostfix(s)
print(postfix)
prefix=postfixToPrefix(postfix)
print(prefix)
