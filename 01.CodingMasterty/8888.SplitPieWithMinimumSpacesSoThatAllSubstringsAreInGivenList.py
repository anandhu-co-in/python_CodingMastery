# Copyright : Rachit AlgoExpert Yt.
# Warning : This piece of code involves some crazy recursion plus some dynamic programming
# You need to find the minimum no of spaces using which you can split PI so that all substrings exists in IN

PI = "314159265358979323846263383279"
IN = ['314', '49', '9001', '15926535897', '14', '9323', '846263383279', '4', '793']


# PI = '12345'
# IN = ['1','2','3','5','345']

def pos(p):
    ans = None
    # Search for Every Possible Substring starting form position post, that is present in IN
    for i in range(p + 1, len(PI) + 1):
        # Whenever a match is found
        if PI[p:i] in IN:
            # If the match is found with the whole string, we got the best solution!
            if i == len(PI):
                return 0
            # Otherwise try to split the remaining string  as well, using a crazy  recursive call!
            sub = pos(i)
            if sub is not None:
                if ans is None:
                    ans = 1 + sub
                else:
                    # Maintain the minimum answer for all the matches
                    ans = min(ans, 1 + sub)
    return ans


print(pos(0))

# NOTE
# 1. In python PI[p:i] will print from position p to i-1 <-- i found this a bit tricky

# Dumb
# print("P[{}:{}]={}".format(p, i, PI[p:i]))
# I need to find a way to print the splitted string
# Code should be optimized using dynamic programming
# Code should be optimized using hash tables
# Git commit pending
