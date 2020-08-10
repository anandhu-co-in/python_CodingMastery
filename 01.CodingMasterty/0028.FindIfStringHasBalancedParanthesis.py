# Write a function to check if an input string has balanced parenthesis:


def findIfBalanced(str):
    # Lets use a stack to do this
    stack = []

    # Scan each character
    for x in str:

        # If opening parenthesis push it to stack
        if x == '(':
            stack.append(x)

        # If closing parenthesis, pop one opening one from top, if not present, paranthesis aren't balanced
        elif x == ')':
            if len(stack) == 0:
                return False
            stack.pop()

    # If there are still opening parenthesis left in stack, then the string is not balanced!
    if len(stack) != 0:
        return False
    return True


myString = "Hello how are you((((()))))";
print(findIfBalanced(myString));
